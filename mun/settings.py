"""
Django settings for mun project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't2-a2v5h0rw-f(e6)9-o91+za2)g3cto(in-06!k!j91v8o5x%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'mun-production.cwtqtvgfqj.eu-west-1.elasticbeanstalk.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'pages',
    'users',
    'integrations',
    'notifications',
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

ROOT_URLCONF = 'mun.urls'

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

WSGI_APPLICATION = 'mun.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('RDS_DB_NAME'),
            'USER': os.environ.get('RDS_USERNAME'),
            'PASSWORD': os.environ.get('RDS_PASSWORD'),
            'HOST': os.environ.get('RDS_HOSTNAME'),
            'PORT': os.environ.get('RDS_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DATABASE_NAME', ''),
            'USER': os.environ.get('DATABASE_USER', ''),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
            'HOST': os.environ.get('DATABASE_HOST', ''),
            'PORT': os.environ.get('DATABASE_PORT', ''),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/releases'
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'integrations.pipeline.save_integration',
    'notifications.pipeline.create_default_notifications',
)

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.google.GooglePlusAuth',
    'social_core.backends.spotify.SpotifyOAuth2',
    'social_core.backends.deezer.DeezerOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# SOCIAL_AUTH_GOOGLE_PLUS_KEY = os.environ.get('GOOGLE_PLUS_KEY', '')
# SOCIAL_AUTH_GOOGLE_PLUS_SECRET = os.environ.get('GOOGLE_PLUS_SECRET', '')

SOCIAL_AUTH_SPOTIFY_KEY = os.environ.get('SPOTIFY_KEY', '')
SOCIAL_AUTH_SPOTIFY_SECRET = os.environ.get('SPOTIFY_SECRET', '')
SOCIAL_AUTH_SPOTIFY_SCOPE = ['user-read-email', 'user-follow-read']

SOCIAL_AUTH_DEEZER_KEY = os.environ.get('DEEZER_KEY', '')
SOCIAL_AUTH_DEEZER_SECRET = os.environ.get('DEEZER_SECRET', '')
SOCIAL_AUTH_DEEZER_SCOPE = ['basic_access', 'email']


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
