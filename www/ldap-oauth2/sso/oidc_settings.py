OIDC_ISSUER = "https://sso-uat.iitb.ac.in"
OIDC_RP_CLIENT_ID = "wmciitbombay"  # os.environ.get("OIDC_CLIENT_ID")
# os.environ.get("OIDC_CLIENT_SECRET")
OIDC_RP_CLIENT_SECRET = "eOKduVz0Jgh7ZcBGngMNtfJ3jHY18g49V7DvT76C"
OIDC_OP_AUTHORIZATION_ENDPOINT = "https://sso-uat.iitb.ac.in/authorize"
OIDC_OP_TOKEN_ENDPOINT = "https://sso-uat.iitb.ac.in/token"
OIDC_OP_USER_ENDPOINT = "https://sso-uat.iitb.ac.in/user"
OIDC_RP_SCOPE = "openid"
OIDC_RP_SIGN_ALGO = "RS256"
OIDC_OP_JWKS_ENDPOINT = "https://sso-uat.iitb.ac.in/.well-known/jwks.json"
LOGIN_REDIRECT_URL = "user:home"
LOGOUT_REDIRECT_URL = "index"

OIDC_REMOTE_USER_CLAIM = "uid"
OIDC_VERIFY_KID = False

# For original package
# def generate_username(email):
#     print(f"username[email] = {email}")
#     return email.split("@")[0]

def generate_username(claims):
    print(f"username[claims] = {claims.get(OIDC_REMOTE_USER_CLAIM)}")
    return claims.get(OIDC_REMOTE_USER_CLAIM, claims.get('email', '').split("@")[0])

OIDC_USERNAME_ALGO = generate_username

OIDC_AUTHENTICATION_CALLBACK_URL = "oidc_authentication_callback"


OIDC_CRYPTO_PASSPHRASE = "894U8QxUorYpPOobQ7wW"
OIDC_SSL_VALIDATE_SERVER = False
OIDC_COOKIE_PATH = "/"
OIDC_SESSION_MAX_DURATION = 600
OIDC_STATE_TIMEOUT = 3600

OIDC_RESPONSE_TYPES_SUPPORTED = ["code"]
OIDC_TOKEN_ENDPOINT_AUTH_METHODS_SUPPORTED = ["client_secret_basic"]

# OIDC_PROVIDER_METADATA_URL = "https://sso-uat.iitb.ac.in/.well-known/openid-configuration"
# OIDC_REDIRECT_URI = "http://127.0.0.1:8000/user/"
# OIDC_CODE_TOKEN_EXCHANGE_URI = "http://127.0.0.1:8000/oidc/token_exchange"
# # os.environ.get("OIDC_CRYPTO_PASSPHRASE")
# OIDC_SCOPES_SUPPORTED = ["openid"]
# OIDC_JWT_KEYS = [
#     {
#         "kid": "sso",
#         "kty": "RSA",
#         "n": "czgB1AxXvIVVcwDY3TNiD98PQ9FhDxEGHIzDvFt72bs2rmIEM8oldEx6IoBhUXAXpS2cihOhM2DMa9qSvsGOXw",
#         "e": "AQAB"
#     }
# ]
# protected_urls = [
#     "/user/",
#     "/oauth/applications/",
#     "/oauth/authorize/",
#     "/account/logout/",
#     "/admin/",
# ]
