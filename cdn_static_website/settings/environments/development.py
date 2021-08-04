# -*- coding: utf-8 -*-

"""
This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""

import logging
from typing import List

from cdn_static_website.settings.components import config
from cdn_static_website.settings.components.middleware import MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
]

MIDDLEWARE += ()
