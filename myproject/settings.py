"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '29dou)h$xto=ft%qtd5p_dwnsxh9f9m45+=+5qf1+!z0hbkukl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SESSION_IDLE_TIMEOUT = 3600

# Application definition

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django.contrib.admindocs',
    'django-session-idle-timeout',
    'south',
    'webform',
    'django_countries',
    'easy_pdf',
    'dash',
    'insurance',
    'django_object_actions',
    'alphafilter',
)

RECAPTCHA_PUBLIC_KEY = '6LdQiPYSAAAAAB-hcaIta92MUxjcCknDAH4UtZUX'
RECAPTCHA_PRIVATE_KEY = '6LdQiPYSAAAAAIZJmbvN1DFuH2yLnNJUmm-1o0XS'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django-session-idle-timeout.middleware.SessionIdleTimeout',
)

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'
TEMPLATE_DIRECTORY = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abidatabase',
        'USER': 'abisingapore',
        'PASSWORD': 'abisingapore123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

STATICFILES_DIRS = (
    '/home/abisingapore/webapps/cvdatabase/myproject/webform/static',
)


STATIC_ROOT = "/home/abisingapore/webapps/staticapp/"

MEDIA_ROOT = "/home/abisingapore/webapps/staticapp/files/"

MEDIA_URL = "/media/"

DATE_INPUT_FORMATS = ('%d %b %Y','%d %b, %Y')

GRAPPELLI_INDEX_DASHBOARD = 'myproject.dashboard.CustomIndexDashboard'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = 'http://abisingapore.webfactional.com/static/'


GRAPPELLI_ADMIN_TITLE = "Human Resources Manager"
