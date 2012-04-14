import os

ROOT = os.path.abspath('./jamiecurle')


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jamie', 'me@jamiecurle.co.uk'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'jamiecurle3',
        'USER': 'jcurle',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
USE_I18N = False
USE_L10N = False
USE_TZ = False
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
MEDIA_ROOT = '%s/media/' % ROOT
MEDIA_URL = '/media/'
STATIC_ROOT = '%s/static/' % ROOT
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '%s/admin/' % STATIC_URL
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

SECRET_KEY = 'therealoneisinthelocalsettings'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    #'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'jamiecurle.context_processors.disqus_developer'
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jamiecurle.urls'

#WSGI_APPLICATION = 'jamiecurle.wsgi.application'

TEMPLATE_DIRS = (
   '%s/templates/' % ROOT
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'omblog',
    'compressor',
    'gunicorn',
    'jamiecurle.apps.utils'
)

DATE_FORMAT = "j F Y"

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/x-sass', '/usr/bin/sass {infile} {outfile}'),
)
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': '',
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

#WSGI_APPLICATION = 'jamiecurle.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
