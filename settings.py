# -*- coding:utf-8 -*-
# Django settings for money project.

# NOTE:
# Copy settings.py to settings.py and change all lines containing ***
# (they will cause Python syntax errors if not modified).

import os

RUNNING_WSGI = (os.environ.get('RUNNING_WSGI') == 'true')

SHOW_DEBUG_TOOLBAR = RUNNING_WSGI

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },

    },
]

DATABASES = {
    # This is the gnucash_django database connection.  It holds database tables that are NOT used by GnuCash.
    # (They can't be stored in the same database because GnuCash will delete unrecognized tables.)
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gnucash_django',  # Or path to database file if using sqlite3.
        'USER': 'mysql',  # Not used with sqlite3.
        'PASSWORD': '123456',  # Not used with sqlite3.
        'HOST': '172.16.50.112',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    },

    # This is the GnuCash database connection.  It holds the database tables that are used by GnuCash.  The
    # application will read the transactions and other data in these tables, and perform limited modifications.
    'gnucash': {
        'ENGINE': 'django.db.backends.mysql',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gnucash',  # Or path to database file if using sqlite3.
        'USER': 'mysql',  # Not used with sqlite3.
        'PASSWORD': '123456',  # Not used with sqlite3.
        'HOST': '172.16.50.112',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    }
}

DATABASE_ROUTERS = ['gnucash_data.gnucash_db_router.GnucashDataRouter']

GNUCASH_CONN_STRING = 'mysql://mysql:123456@172.16.50.112:3306/gnucash'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

if RUNNING_WSGI:
    BASE_URL = os.environ['WSGI_SCRIPT_NAME'].rstrip('/')
else:
    BASE_URL = ''

STATIC_URL = BASE_URL + '/static/'

STATIC_ROOT = 'static'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ('0ZBZHTxqfwOVTowFjGf49E9r9z8DMmYJj9ok7yHSYA1e05kobiOY076DBPOyj5pe')

LOGIN_URL = BASE_URL + '/accounts/login/'

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     #     'django.template.loaders.eggs.Loader',
# )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'middleware.middleware.ClearCachesMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    'django.contrib.staticfiles',  # only available in Django 1.3+

    'gnucash_data.apps.GnucashDataConfig',
    'gnucash_scripts',
    'utils',
    'money_templates',
    'money_views',
)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     'django.core.context_processors.static',
#     'django.contrib.messages.context_processors.messages',
#
#     'django.core.context_processors.request',
# )

ACCOUNTS_LIST = [
    # (***GNUCASH ACCOUNT PATH***),
    'Assets:Current Assets:BANK ACCOUNT NAME',
]

NUM_MERCHANTS_BATCH_CATEGORIZE = 50
NUM_TRANSACTIONS_PER_PAGE = 50

# This feature requires a little more setup.  Namely, the GnuCash API must be
# properly set up (which generally requires building GnuCash from source) and
# it must be made available to the application's virtualenv.  Also, the user
# running the application must have write access to the gnucash_api_home/
# directory.
ENABLE_ADD_TRANSACTIONS = False

if SHOW_DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    INTERNAL_IPS = ('127.0.0.1')

WSGI_APPLICATION = 'wsgi.application'
