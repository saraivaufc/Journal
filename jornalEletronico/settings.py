"""
Django settings for jornalEletronico project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's^3v=-=cs-5b1_a+bx%j6(=wdq!k&gnn4g++qtxu*%ada2hjrl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'newspaper',
    'rosetta',
)

INSTALLED_APPS += (
    'djconfig',
)

DJC_BACKEND = 'djconfig'

TEMPLATE_DIRS = (
    'newspaper/templates',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


ROOT_URLCONF = 'newspaper.urls'


ST_RATELIMIT_ENABLE = True
ST_RATELIMIT_CACHE_PREFIX = 'srl'
ST_RATELIMIT_CACHE = 'default'


ROOT_URLCONF = 'jornalEletronico.urls'



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'newspaper_cache',
    },
}

CACHES.update({
    'djconfig': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
})



WSGI_APPLICATION = 'jornalEletronico.wsgi.application'

AUTH_USER_MODEL = 'newspaper.UserAuthenticated'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'postgres' : {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'newspaper',                      
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
        ('pt', ('Portuguese')),
        ('en', ('English')),
        ('es', ('Spanish')),
)

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

PROJECT_DIR = os.path.dirname(__file__)

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../newspaper/static'),)


LOCALE_PATHS = (
        os.path.join(PROJECT_DIR, '../newspaper/locale'),
        '/var/local/translations/locale',
)

MEDIA_ROOT= os.path.join(PROJECT_DIR, '../media')
MEDIA_URL='/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '.')
STATIC_URL = '/static/'

#settings email
EMAIL_ADMINS = ['saraiva.ufc@gmail.com','saraiva@alu.ufc.br']

