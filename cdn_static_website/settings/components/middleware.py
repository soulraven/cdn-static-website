#  -*- coding: utf-8 -*-

from typing import Tuple

MIDDLEWARE: Tuple[str, ...] = (
    # Content Security Policy:
    # 'csp.middleware.CSPMiddleware',
    # Django:
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # django-maintenance-mode
    # 'maintenance_mode.middleware.MaintenanceModeMiddleware',
    # 'pg_flash_messages.middleware.FlashMessagesMiddleware'

)
