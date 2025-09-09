from flask import Flask, request
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SP1 Home</h1>
    <a href="/login">Login via IdP</a><br>
    <a href="http://localhost:8000/logout">Logout</a>
    """

@app.route("/login")
def login():
    return '<a href="http://localhost:8000/sso?acs=http://localhost:8002/acs">Login via IdP</a>'

@app.route("/acs", methods=["POST"])
def acs():
    saml_response = request.form.get("SAMLResponse")
    xml = base64.b64decode(saml_response).decode()
    return f"<h2>SP2 received SAML Response:</h2><pre>{xml}</pre><br><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(port=8002)

