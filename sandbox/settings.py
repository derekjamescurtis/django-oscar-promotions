import os

from oscar.defaults import *  # noqa


# Path helper
def base_location(location):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), location)


ALLOWED_HOSTS = [
    'latest.oscarcommerce.com',
    'master.oscarcommerce.com',
    'localhost',
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DATABASE_NAME', 'promotions'),
        'USER': os.environ.get('DATABASE_USER', 'promotions'),
        'PASSWORD': os.environ.get('DATABASE_USER', 'promotions'),
    }
}

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    # Oscar apps
    'oscar',
    'oscar.apps.analytics',
    'oscar.apps.checkout',
    'oscar.apps.address',
    'oscar.apps.shipping',
    'oscar.apps.catalogue',
    'oscar.apps.catalogue.reviews',
    'oscar.apps.partner',
    'oscar.apps.basket',
    'oscar.apps.payment',
    'oscar.apps.offer',
    'oscar.apps.order',
    'oscar.apps.customer',
    'oscar.apps.search',
    'oscar.apps.voucher',
    'oscar.apps.wishlists',
    'tests._site.apps.dashboard',
    'oscar.apps.dashboard.reports',
    'oscar.apps.dashboard.users',
    'oscar.apps.dashboard.orders',
    'oscar.apps.dashboard.catalogue',
    'oscar.apps.dashboard.offers',
    'oscar.apps.dashboard.partners',
    'oscar.apps.dashboard.pages',
    'oscar.apps.dashboard.ranges',
    'oscar.apps.dashboard.reviews',
    'oscar.apps.dashboard.vouchers',
    'oscar.apps.dashboard.communications',
    'oscar.apps.dashboard.shipping',
    # Oscar promotions apps
    'oscar_promotions',
    'oscar_promotions.dashboard',
    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'easy_thumbnails',
    'django_tables2',
    'django_extensions',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [base_location('templates')],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.core.context_processors.metadata',
                'oscar_promotions.context_processors.promotions',
            ],
        },
    }
]


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 6},
    },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

HAYSTACK_CONNECTIONS = {
    'default': {'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'}
}
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
ROOT_URLCONF = 'sandbox.urls'
LOGIN_REDIRECT_URL = '/accounts/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
PUBLIC_ROOT = base_location('public')
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')
DEBUG = True
SITE_ID = 1
USE_TZ = 1
APPEND_SLASH = True
LANGUAGE_CODE = 'en-gb'

SECRET_KEY = 'notverysecret'
