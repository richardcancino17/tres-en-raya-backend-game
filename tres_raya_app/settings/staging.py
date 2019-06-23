from .base import *

ALLOWED_HOSTS = ['178.128.9.218','127.0.0.1','localhost']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'chatydb',
        'USER': 'postgres',
        'PASSWORD': '992424558',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
APPSECRET_PROOF = False

