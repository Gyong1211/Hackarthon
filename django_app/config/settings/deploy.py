from config.settings.base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

WSGI_APPLICATION = 'config.wsgi.deploy.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['s3_bucket_name']
AWS_S3_REGION_NAME = config_secret_deploy['aws']['s3_region_name']
# AWS_S3_SIGNATURE_VERSION = config_secret_deploy['aws']['s3_signature_version']
S3_USE_SIGV4 = True

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
DATABASES = config_secret_deploy['django']['databases']