# -*- coding: utf-8 -*-
import rollbar
from django_rest_example.settings.base import *

DEBUG = True

BASE_URL = 'http://api.devslaw.com/'
CLIENT_BASE_URL = 'http://devslaw.com/'
ALLOWED_HOSTS = ['*', ]

BASE_PATH = "/var/www/django_rest_example"

THIRD_PARTY_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE_CLASSES += [
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + PROJECT_APPS

ROLLBAR = {
    'access_token': os.environ.get('ROLLBAR_ACCESS_TOKEN', ''),
    'environment': 'development' if DEBUG else 'production',
    'root': BASE_DIR,
}
rollbar.init(**ROLLBAR)
