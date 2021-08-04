# -*- coding: utf-8 -*-

import os

from cdn_static_website.settings.components import BASE_DIR, config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.joinpath('db.sqlite3').as_posix(),
    }
}
