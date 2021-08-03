# -*- coding: utf-8 -*-

import os
import sys

INTERP = "/opt/workzone/.virtualenvs/cdn-static-website/bin/python3"
# INTERP is present twice so that the new python interpreter
# knows the actual executable path
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/cdn_static_website')  # You must add your project here

sys.path.insert(0, '/opt/workzone/.virtualenvs/cdn-static-website/bin')
sys.path.insert(0, '/opt/workzone/.virtualenvs/cdn-static-website/lib/python3.9/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "cdn_static_website.settings"
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from django.db.backends.signals import connection_created
from django.dispatch import receiver


@receiver(connection_created)
def setup_postgres(connection, **kwargs):
    if connection.vendor != 'postgresql':
        return

    # Timeout statements after 30 seconds.
    with connection.cursor() as cursor:
        cursor.execute("""
            SET statement_timeout TO 30000;
        """)
