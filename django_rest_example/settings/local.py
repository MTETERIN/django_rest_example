# -*- coding: utf-8 -*-
from django_rest_example.settings.base import *

DEBUG = True

BASE_URL = 'http://127.0.0.1:8000/'
CLIENT_BASE_URL = 'http://devslaw.dev/'
ALLOWED_HOSTS = ['*', ]

BASE_PATH = "/var/www/django_rest_example/"

THIRD_PARTY_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + PROJECT_APPS
