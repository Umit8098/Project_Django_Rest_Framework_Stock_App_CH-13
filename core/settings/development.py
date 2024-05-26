from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    # Extras for Debug
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# DebugToolBar
INTERNAL_IPS = [
    "127.0.0.1", 
]

# LOGGING
# https://docs.djangoproject.com/en/4.0/topics/logging/#logging
'''
    DEBUG: Hata ayıklama amaçlı düşük seviyeli sistem bilgisi.
    INFO: Genel sistem bilgisi.
    WARNING: Küçük çaplı hataların bilgisi.
    ERROR: Büyük çalplı hataların bilgisi.
    CRITICAL: Kritik hataların bilgisi.
'''
LOGGING = { 
    "version": 1, 
    # is set to True then all loggers from the default configuration will be disabled. 
    "disable_existing_loggers": True, 
    # Formatters describe the exact format of that text of a log record.  
    "formatters": { 
        "standard": { 
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s" 
        }, 
        'verbose': { 
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}', 
            'style': '{', 
        }, 
        'simple': { 
            'format': '{levelname} {message}', 
            'style': '{', 
        }, 
    }, 
    # The handler is the engine that determines what happens to each message in a logger. 
    # It describes a particular logging behavior, such as writing a message to the screen,  
    # to a file, or to a network socket. 
    "handlers": { 
        "console": { 
            "class": "logging.StreamHandler", 
            "formatter": "standard", 
            "level": "INFO", 
            # "level": "ERROR",
            # "level": config("DJANGO_LOG_LEVEL", "INFO"), 
            # "level": config("DJANGO_LOG_LEVEL"), 
            "stream": "ext://sys.stdout", 
            }, 
        'file': { 
            'class': 'logging.FileHandler', 
            "formatter": "verbose", 
            'filename': './debug.log', 
            'level': 'INFO', 
            # 'level': 'ERROR',
            # "level": config("DJANGO_LOG_LEVEL", "INFO"), 
            # "level": config("DJANGO_LOG_LEVEL"), 
        }, 
    }, 
    # A logger is the entry point into the logging system. 
    "loggers": { 
        "django": { 
            "handlers": ["console", 'file'], 
            # log level describes the severity of the messages that the logger will handle.  
            # "level": "INFO",  
            # "level": "WARNING",  
            # "level": config("DJANGO_LOG_LEVEL"),  
            "level": config("DJANGO_LOG_LEVEL", "INFO"),  
            # "level": config("DJANGO_LOG_LEVEL", "WARNING"),  
            'propagate': True, 
            # If False, this means that log messages written to django.request  
            # will not be handled by the django logger. 
        }, 
    }, 
}
