from .base import (
    ALLOWED_HOSTS, INSTALLED_APPS, MIDDLEWARE,
)
from .base import *  # NOQA

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#p6nn)whgu**7l*(#b65za&e^bs6=l1kvc59&vruo3h0x+^poa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS += ['127.0.0.1']


# debug_toolbar settings

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = '127.0.0.1'
