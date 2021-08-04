# -*- coding: utf-8 -*-

import logging

from django.conf import settings


class RequireDebugFalse(logging.Filter):

    def filter(self, records):
        return not settings.DEBUG


class RequireDebugTrue(logging.Filter):

    def filter(self, record):
        return settings.DEBUG
