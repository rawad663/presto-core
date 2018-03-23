"""
Django settings for Presto project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Allow all host headers

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z85y#$w_9o=kl++$&95=)+4%b%3z+*9%=&#ev$j49o-a_^i-1='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '0.0.0.0', 'presto-core.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'restos.apps.RestosConfig',
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

ROOT_URLCONF = 'Presto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Presto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#import dj_database_url
#import os

#ON_HEROKU = os.environ.get('ON_HEROKU')

'''if ON_HEROKU:
    DATABASE_URL = 'postgres://phjtvicgngzvmj:c4cf7232fc629ce6454c598a8030d54d30df68f3f922328eacef8b47227b090b@ec2-107-20-249-48.compute-1.amazonaws.com:5432/dq2ualop41h4e'
    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True, default=DATABASE_URL)}
else:
    DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}'''

# # If running on heroku
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql_psycopg2',
#          'NAME': 'dq2ualop41h4e',
#          'USER': 'phjtvicgngzvmj',
#          'PASSWORD': 'c4cf7232fc629ce6454c598a8030d54d30df68f3f922328eacef8b47227b090b',
#          'HOST': 'ec2-107-20-249-48.compute-1.amazonaws.com',
#          'PORT': '5432',
#      }
# }

#if running locally
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'restos.User'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
