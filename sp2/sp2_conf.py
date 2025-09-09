

from onelogin.saml2.settings import OneLogin_Saml2_Settings

SAML_SETTINGS = {
    "strict": True,
    "sp": {
        "entityId": "http://localhost:8002/metadata/",
        "assertionConsumerService": {
            "url": "http://localhost:8002/acs/",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
        },
        "x509cert": "",
        "privateKey": open("../sp2/certs/sp2_private.key").read()
    },
    "idp": {
        "entityId": "http://localhost:8000/idp",
        "singleSignOnService": {
            "url": "http://localhost:8000/sso",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
        },
        "x509cert": open("../idp/certs/idp_cert.pem").read()
    }
}
SAML_SETTINGS = OneLogin_Saml2_Settings(settings=SAML_SETTINGS)
