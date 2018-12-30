"""
Django settings for vanilla_arcade project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tromw#)jg98nbzr0i-%ibvof7un!52%r*6z-s!$=by%jr@nz)6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first_app',
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

ROOT_URLCONF = 'vanilla_arcade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'vanilla_arcade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR = [
    os.path.join(BASE_DIR,'static'),
    '/var/www/static/',
]
MEDIA_URL = '/media/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
print(MEDIA_ROOT)

# SEND_GRID_API_KEY = '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'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = '587'
# EMAIL_HOST_USER = 'vanillaarcade'
# EMAIL_HOST_PASSWORD = 'Qwerty42!'
# #For gmail or google apps
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# DEFAULT_FROM_EMAIL = 'saadgauhar@gmail.com'
# ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Contact email received from website'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# ------ GMAIL EMAILS -------
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'server@vanillaarcade.com'
EMAIL_HOST_PASSWORD = 'kwofmqvdonyjcors'   #alkdoqqyzoleeivs
#For gmail or google apps
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False