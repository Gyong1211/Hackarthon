from config.settings.base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

WSGI_APPLICATION = 'config.wsgi.debug.application'

INSTALLED_APPS.append('django_extensions')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')


DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}