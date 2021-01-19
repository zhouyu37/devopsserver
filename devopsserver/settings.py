"""
Django settings for devopsserver project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2h1g#9uv*b8$t&rdczr+-k#q%+ntf$osr@@-_b3wd%03yv1#^^'

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
    'rest_framework',
    'api.apps.ApiConfig',
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

ROOT_URLCONF = 'devopsserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'devopsserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'opendevops',
        'USER':'zhou',
        'PASSWORD':'123',
        'HOST':'10.110.152.159',
        'PORT':3306,
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

ALLOWED_HOSTS = ['*']

PRIV_KEY = b'LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlDWUFJQkFBS0JnUUNnalJJQlB0Q1Vsc09zUlVlOFhZWGVyNnM1RDlhemFsd3ZRbENYQ1U1OStuZXFZV0ZkCkRSRGZucjllK3hVTmwxTDRybDFIYkw3WStMci9RdWM4WFI4aG1zbGdYN2l2eE93am9NakFDc1RxQmY2WWt5Sk8KS0RrbSs0N1VzTC9DYUpZb3B1NDFUT1AxZ0F3dkR3dHZNVW96RmMyZEtCS2E1NTZ6U3ltbGlHRzYvUUlEQVFBQgpBb0dBTDgvekpiWE1MZ1A3LzhpZUJXV2dvV0dWVHlmOVcyNzRSd2FyczE4TkpnMDZKOTVhUFhqUHBwakRDd2toCkN1d2V4SHBBd3kyS1pGa21iekJBSG9mS04xZ2Q5Y2hmTmxESEErUEFyS01NSWVyem8wMWRNaU00bWhGejhSMksKQVBqdmQycWo0azRYaFNJOU1EMEI1Ym1RRHY4bWJDZzlxL2pRejRlNmhETG0zYUVDUlFEeWtldUFmS3Foem5rMQpPcTJmcXFjUjZwQlpLT0U5Q2V6aEdhOTdQNHRyMWRNVXo3TW00RVptQ0RhMGh2d2QzQWJMb3hLOG1CTXhZUGE2Cmk5eTg5TkNwNWNtaHFRSTlBS2x3cG0yRWFSUmNqbWNBRkdoZWVWN0d6ek5IcmRJaXMwd1ZNYnNQeno0NGFhRUcKcUszUStoMmttVTJjR0J0cVhaWXpXdDViQTdsMUxza0xOUUpFYnkyK2VSZXF4WnJ6SnhpTDk4Q3A3cVpLSHZPRAp1UXhSakNMUHNYZkFtVjVaN3hIN2xQZjZqRTE3ZFdiaEszWnJqdTVoYWh0eHdKSW13LzNTNExCODYwSXRGbkVDClBEN0paSkorbDJXWktwZVdXdm1WMEluRFIvSnJwRWlTM1RmYlByTmZsMThxRGxKQ0ltMU9XL0J5RnZEQVg5cUEKM3E4UzFxQkF2NitRY2NiRDVRSkZBT3lHbFljNkdGai9PT1JPakZiRWZ1U0JXMitsQUdlZ3owZk9IUWVQRGw1bAphNmtFR1Rmc21BM3gyRkVLNFVmVlpGbUcxQU15RU5hdU1oZ1VHaHcyL3ZFMWpqZ2QKLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0K'

URL_AUTH_KEY="helloworld"

SECRET_KEY="helloworld1!"