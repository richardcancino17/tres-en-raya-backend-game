from .base import *

ALLOWED_HOSTS = ['account.brainred.com','209.97.136.148','127.0.0.1','localhost']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'abbottdb',
        'USER': 'postgres',
        'PASSWORD': '992424558',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
APPSECRET_PROOF = False
