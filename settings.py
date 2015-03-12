"""
These settings are used by the ``manage.py`` command.

"""
import os

DEBUG = True

SITE_ID = 1

USE_TZ = True
TIME_ZONE = 'UTC'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}

INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'django_bnr'
]


ROOT_URLCONF = 'urls'
PROJECT_ROOT = os.path.dirname(__file__)
STATIC_URL = '/static/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = 'secret'

from django.utils.log import DEFAULT_LOGGING as LOGGING

LOGGING['loggers']['django'] = {
    'level': 'DEBUG',
    'handlers': ['console']
}

LOGGING['loggers']['django.security'] = {
    'level': 'DEBUG',
    'handlers': ['console']
}
