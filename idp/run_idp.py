from flask import Flask, request, session
import base64, datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"   # needed for sessions


@app.route("/sso", methods=["GET", "POST"])
def sso():
    acs_url = request.args.get("acs") or request.form.get("acs")

    # If user already logged in, skip login form
    if "username" in session and request.method == "GET":
        return make_saml_response(session["username"], acs_url)

    if request.method == "GET":
        # First time, show login form
        return f"""
        <form method="post">
            <input type="hidden" name="acs" value="{acs_url}">
            <input type="text" name="username" placeholder="Enter username">
            <button type="submit">Login</button>
        </form>
        <br>
        <a href="/logout">Logout</a>
        """

    elif request.method == "POST":
        # User submitted login form
        username = request.form.get("username")
        session["username"] = username
        return make_saml_response(username, acs_url)


@app.route("/logout")
def logout():
    """Clear the IdP session and show logout confirmation."""
    session.clear()
    return """
    <p>You have been logged out of IdP.</p>
    <a href="/sso">Login again</a>
    """



def make_saml_response(username, acs_url):
    """Generate a fake base64-encoded SAML Response and post back to SP."""
    now = datetime.datetime.utcnow().isoformat() + "Z"

    saml_response = f"""
    <samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
        ID="_id123" Version="2.0" IssueInstant="{now}"
        Destination="{acs_url}">
        <saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">idp.example.com</saml:Issuer>
        <samlp:Status>
            <samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
        </samlp:Status>
        <saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
            ID="_assertion123" IssueInstant="{now}" Version="2.0">
            <saml:Subject>
                <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">{username}</saml:NameID>
            </saml:Subject>
        </saml:Assertion>
    </samlp:Response>
    """

    b64_response = base64.b64encode(saml_response.encode()).decode()

    return f"""
    <html><body onload="document.forms[0].submit()">
    <form method="post" action="{acs_url}">
        <input type="hidden" name="SAMLResponse" value="{b64_response}"/>
    </form>
    </body></html>
    """


if __name__ == "__main__":
    app.run(port=8000)
