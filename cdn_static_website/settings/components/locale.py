# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as ugt

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

USE_I18N = True
USE_L10N = True

# https://docs.djangoproject.com/en/3.2/ref/settings/#languages
LANGUAGES = (
    ('en', ugt('English')),
)

# https://docs.djangoproject.com/en/3.2/ref/settings/#locale-paths
LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'UTC'

# https://docs.djangoproject.com/en/3.2/ref/settings/#first-day-of-week
FIRST_DAY_OF_WEEK = 1
