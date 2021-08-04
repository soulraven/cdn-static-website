#  -*- coding: utf-8 -*-

# Templates
# https://docs.djangoproject.com/en/3.2/ref/templates/api/

from cdn_static_website.settings.components import BASE_DIR, config

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        BASE_DIR.joinpath('templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # Default template context processors:
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },
}]
