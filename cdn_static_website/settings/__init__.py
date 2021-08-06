# -*- coding: utf-8 -*-

from os import environ
from split_settings.tools import optional, include

# Managing environment via DJANGO_ENV variable:
environ.setdefault('DJ_DEV_ENV', 'development')
ENV = environ['DJ_DEV_ENV']

base_settings = [
    'components/apps.py',
    'components/common.py',
    'components/database.py',
    'components/logging.py',
    'components/caches.py',
    'components/middleware.py',
    'components/templates.py',
    'components/locale.py',
    'components/security.py',
    'components/static.py',

    # Select the right env:
    'environments/{0}.py'.format(ENV),
    # Optionally override some settings:
    optional('environments/local.py'),
]

# Include settings:
include(*base_settings)
