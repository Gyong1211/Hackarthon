from utils.key import aa
from .base import *

DEBUG = True
config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

INSTALLED_APPS.append('django_extensions')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_DIR,
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

WSGI_APPLICATION = 'config.wsgi.debug.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hackarthon',
        'USER': 'daham',
        'PASSWORD': aa,
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

print('@@@@@@@@@@@@@@@ DEBUG: debuggggggggggg', DEBUG)
print('@@@@@@@@@@@@@@@ ALLOWED_HOSTS: ', ALLOWED_HOSTS)
