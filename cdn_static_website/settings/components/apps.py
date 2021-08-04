#  -*- coding: utf-8 -*-

from typing import Tuple

PREREQ_APPS: Tuple[str, ...] = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Django Extensions is a collection of custom extensions for the Django Framework.
    # see: Django Extensions is a collection of custom extensions for the Django Framework.
    'django_extensions',
)

PROJECT_APPS: Tuple[str, ...] = ()

# Application definition
INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS
