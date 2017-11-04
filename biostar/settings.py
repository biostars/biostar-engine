import os

# Apply the logger settings.
from biostar.logconf import LOGGING

SITE_ID = 1
SITE_DOMAIN = "localhost"
SITE_NAME = "Biostar Engine"
SITE_HEADER = '<i class="barcode icon"></i> Bioinformatics Recipes'


def join(*args):
    return os.path.abspath(os.path.join(*args))


ADMINS = [
    ("Admin User", "1@lvh.me")
]

ADMIN_GROUP_NAME = "Admins"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(join(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1@lvh.me'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
COMPRESS_ENABLED = True

# Application definition
PROTOCOL = "http"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mailer',
    'compressor',
    'pagedown',
    'biostar.emailer',
    'biostar.engine.apps.EngineConfig',
    'biostar.accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'biostar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'string_if_invalid': "**MISSING**",
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'biostar.engine.context.engine',

            ],
        },
    },
]

WSGI_APPLICATION = 'biostar.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASE_NAME = join(BASE_DIR, '..', 'export', 'database', 'engine.db')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_NAME,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

]

ALLOWED_HOSTS = ['www.lvh.me', 'localhost', '127.0.0.1']

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_ROOT = join(BASE_DIR, '..', 'export', 'media')

# The location of resusable data.
LOCAL_ROOT = join(BASE_DIR, '..', 'export', 'local')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, '..', 'export', 'static')
STATICFILES_DIRS = [
    join(BASE_DIR, "engine", "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

LOGGER_NAME = "biostar.engine"

# We are using django-mailer to store emails in the database.
# EMAIL_BACKEND = "mailer.backend.DbBackend"

# The email delivery engine.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

