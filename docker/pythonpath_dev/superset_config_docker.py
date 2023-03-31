import os
from flask_appbuilder.security.manager import AUTH_OAUTH
from custom_sso_security_manager import CustomSsoSecurityManager

ROW_LIMIT = os.environ['SUPERSET_ROW_LIMIT']
SUPERSET_WORKERS = os.environ['SUPERSET_WORKERS']
SECRET_KEY=os.environ['SECRET_KEY']
SUPERSET_WEBSERVER_PORT = 8088

CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager
basedir = os.path.abspath(os.path.dirname(__file__))
AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Admin" #Change this to make a default role as the user role when registers.
AUTH_ROLE_ADMIN = 'Admin'
PREFERRED_URL_SCHEME = 'http'
OAUTH_PROVIDERS = [
{
        'name':'auth0',
        'token_key': 'access_token',
        'icon':'fa-at',
        'remote_app': {
            'client_id': 'bKm8OYCbTByMpyumSNwYCdQW5sOgaUwP',
            'client_secret': 'FY-JzpNXB9VmKLy5Ak5ZQoP5Nd8ThB9S5w8VrdH933OHAnPHacBRXjhP8bknMfSq',
            'server_metadata_url': os.path.join('https://staging-datalakehouse.us.auth0.com', '.well-known/openid-configuration'),
            'client_kwargs': {'scope': 'openid profile email',},
        'base_url': 'https://staging-datalakehouse.us.auth0.com',
        'access_token_url': 'https://staging-datalakehouse.us.auth0.com/oauth/token',
        'authorize_url': 'https://staging-datalakehouse.us.auth0.com/authorize',
        'access_token_method': 'POST'
        }
   }
]


