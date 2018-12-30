# Example of config.py file
# Missing data needs to be filled in.
# Then save this as instance/config.py

SECRET_KEY = ''

# Request Header Details
API_VERSION = '1.0'
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0'
ACCEPT = 'application/vnd.hmrc.{version}+json'.format(version=API_VERSION)

# The following codes are obtained from the HMRC developers account.
CLIENT_ID = ''
CLIENT_SECRET = ''
SERVER_TOKEN = ''

# Oauth2 Endpoints
AUTHORIZATION_BASE_URL = 'oauth/authorize'
TOKEN_URL = 'oauth/token'
SCOPES = ["read:vat", "write:vat"]

# Redirect URI (set in HMRC developers account)
REDIRECT_URI_TEST = ''

# MTD(VAT) Endpoints
URL_CREATE_TEST_USER = 'create-test-user/organisations'
URL_GET_OBLIGATIONS = 'organisations/vat/{vatno}/obligations'
URL_SUBMIT_VAT = 'organisations/vat/{vatno}/returns'
URL_GET_RETURNS = 'organisations/vat/{vatno}/returns/{period}'
URL_GET_LIABILITIES = 'organisations/vat/{vatno}/liabilities'
URL_GET_PAYMENTS = 'organisations/vat/{vatno}/payments'