"""
Third party settings for local project

"""
from . import environ, INSTALLED_APPS


env = environ.Env()

INSTALLED_APPS += [
    'debug_toolbar',
    'rest_framework',
    'oauth2_provider',
    'drf_spectacular',
    'drf_spectacular_sidecar',
]

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups'
    },

    'RESOURCE_SERVER_INTROSPECTION_URL': env.str('LOCAL_RESOURCE_SERVER_URL'),
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (
        env.str('LOCAL_RESOURCE_SERVER_CLIENT_ID'),
        env.str('LOCAL_RESOURCE_SERVER_CLIENT_SECRET')
    ),
}

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,

    # shorthand to use the sidecar instead
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',

    # Oauth2 related settings. used for example by django-oauth2-toolkit.
    #  https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#oauth-flows-object
    'OAUTH2_FLOWS': ['clientCredentials'],
    'OAUTH2_TOKEN_URL': '/oauth/token/',
    'SERVE_AUTHENTICATION': ['oauth2_provider.contrib.rest_framework.OAuth2Authentication',],
}