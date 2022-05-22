"""
Settings for local project

"""
from . import environ, INSTALLED_APPS


env = environ.Env()


INSTALLED_APPS += [
    'src.apps.account',
]

LOCAL_ADMIN_URL = env('LOCAL_ADMIN_URL')
