# idp_conf.py
from saml2 import BINDING_HTTP_POST
CONFIG = {
    "entityid": "http://localhost:8000/idp",
    "service": {
        "idp": {
            "endpoints": {
                "single_sign_on_service": [
                    ("http://localhost:8000/sso", BINDING_HTTP_POST)
                ],
                "single_logout_service": [
                    ("http://localhost:8000/slo", BINDING_HTTP_POST)
                ]
            },
            "name_id_format": ["urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"],
        }
    },
    "metadata": {
        "local": ["sp1_metadata.xml", "sp2_metadata.xml"]
    },
    "key_file": "../idp/certs/idp_private.key",
    "cert_file": "../idp/certs/idp_cert.pem",
    "organization": {
        "name": "Example IdP",
        "display_name": "Example IdP",
        "url": "http://localhost:8000",
    },
    "contact_person": []
}
