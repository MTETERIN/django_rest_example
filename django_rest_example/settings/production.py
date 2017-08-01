# -*- coding: utf-8 -*-

from django_rest_example.settings.base import *

DEBUG = False

BASE_URL = 'http://api.devslaw.com/'
CLIENT_BASE_URL = 'http://devslaw.com/'
ALLOWED_HOSTS = ['http://devslaw.com/', ]

BASE_PATH = "/var/www/django_rest_example"

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# CORS ORIGIN settings
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'devslaw.com',
)
