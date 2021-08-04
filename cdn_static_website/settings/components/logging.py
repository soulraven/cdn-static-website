# -*- coding: utf-8 -*-

# https://docs.djangoproject.com/en/3.2/topics/logging/

from cdn_static_website.settings.components import BASE_DIR, config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'utils.log_filters.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'utils.log_filters.RequireDebugTrue',
        }
    },
    'formatters': {
        'verbose': {
            'format': (
                    '%(asctime)s [%(process)d] [%(levelname)s] ' +
                    'pathname=%(pathname)s lineno=%(lineno)s ' +
                    'funcname=%(funcName)s %(message)s'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 3,
            'filename': str(BASE_DIR.joinpath(config('FILE_LOGGING_PATH'), 'django.log')),
            'formatter': 'verbose',
            'filters': ['require_debug_true']
        },
        'email_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'console-verbose': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django_file': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['console', 'logfile', 'email_admins'],
            'propagate': True,
            'level': 'INFO',
        },
        'security': {
            'handlers': ['console-verbose', 'logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

