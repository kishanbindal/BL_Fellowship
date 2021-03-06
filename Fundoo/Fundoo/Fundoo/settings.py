import os
from dotenv import load_dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add Template Directory Path here
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
ENV_PATH = os.path.join(BASE_DIR, '.env')
# print('ENV Path : -> ', ENV_PATH)
# print('Base path : -> ', BASE_DIR)
load_dotenv(ENV_PATH)

EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'Fun',
    # 'FundooNotes',
    'FundooNotes.apps.FundoonotesConfig',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
    'django_short_url',
    'storages',
    'django_nose',
    'django_elasticsearch_dsl',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
)

CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:8000',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'token',
]

ROOT_URLCONF = 'Fundoo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Fundoo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': '',
    }
}

AUTH_USER_MODEL = 'Fun.User'  # Come back and change to desired model

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )

SOCIAL_AUTH_GOOGLE_CLIENT_ID = os.getenv('SOCIAL_AUTH_GOOGLE_CLIENTID')
SOCIAL_AUTH_GOOGLE_CLIENT_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_CLIENTSECRET')

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200',
    },
}

#CELERY STUFF
# BROKER_URL = 'amqp://guest@localhost:9092'
# CELERY_RESULT_BACKEND = 'amqp://localhost:9092'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'UTC'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# SWAGGER_SETTINGS = {
#     # 'SHOW_REQUEST_HEADERS': True,
# }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL ='/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')

# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# # NOSE_ARGS = ['--with-spec', '--spec-color']
# NOSE_ARGS = [ '--with-spec', '--spec-color',
#                 # '--with-coverage', '--cover-html',
#                 # '--with-coverage',
#               # '--cover-xml',
#                 # '--cover-package=.',
#                 # '--cover-html-dir=reports/cover'
#                 "--cover-xml-file=FILE",
#
# ]


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# NOSE_ARGS = ['--with-spec', '--spec-color']
NOSE_ARGS = [ '--with-spec', '--spec-color',
# '--with-coverage', '--cover-html',
'--with-coverage', '--cover-xml',
'--cover-package=.',
# '--cover-html-dir=reports/cover'

]