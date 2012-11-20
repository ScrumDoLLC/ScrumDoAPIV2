# Django settings for api_example project.
import os

DEBUG = True



# First, you need to go to http://beta.scrumdo.com/api/v2/oauth/apps register your new app, 
# and fill in the consumer keys here.
CONSUMER_KEY = os.environ.get("CONSUMER_KEY","RJQssf7Fj4LSv6Rjtk")
CONSUMER_SECRET= os.environ.get("CONSUMER_SECRET", "bMLVfEDupKHffFLS6NXE5nUzd9EyWSV7")

# Then, set the hostname of THIS server
HOSTNAME=os.environ.get("HOSTNAME","http://localhost:8001")

# And the hostname of the ScrumDo server you want to contact
SCRUMDO_HOSTNAME=os.environ.get("SCRUMDO_HOSTNAME", "http://localhost:8000")




TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static-build")
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(PROJECT_ROOT, "static"), )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = os.environ.get("SECRET_KEY",'lkds09823-0tjksl;djf-2038')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

SESSION_COOKIE_NAME='api_example_id'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

ROOT_URLCONF = 'api_example.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'api_example.wsgi.application'

TEMPLATE_DIRS = (   os.path.join(PROJECT_ROOT, "templates"),    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'api_example': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}