"""
Django settings for ShareAndPark project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-flihhwy$tc=cy1c8pni&9w))-sf_jr&4h2g16*+glgl1%z3gpg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG"),

ALLOWED_HOSTS = ['0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Дополнительные модули джанго
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.gis',
    # Модули для регистрации, аутентификации, авторизации
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Кастомные фильтры и виджеты
    'django_filters',
    # Стилизация виджетов
    'widget_tweaks',
    # Валидация телефонного номера
    'django_phonenumbers',
    "phonenumber_field",
    # Наше приложение
    'app',
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

ROOT_URLCONF = 'ShareAndPark.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'ShareAndPark.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    #
    # },
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "USER":     os.environ.get("SQL_USER"),                     # "postgres",
        "NAME":     os.environ.get("SQL_DATABASE"),                 # "parking_v2",
        "PASSWORD": os.environ.get("SQL_PASSWORD"),                 # "12345",
        "PORT":     os.environ.get("SQL_PORT"),                     # 5432,
        "HOST":     os.environ.get("SQL_HOST"),                     #'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# ЛОКАЛИЗАЦИЯ ПРОЕКТА
LANGUAGE_CODE = 'ru-RU' #'en-us'
# УСТАНОВКА МОСКОВСКОГО ВРЕМЕНИ
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'

# строка ниже не влияет на отображение если надо удали
STATICFILES_DIRS = [
     BASE_DIR / "static"
 ]

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
# будет использоваться для управления сохраненными данными,
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# REDIRECT SETTINGS
# После авторизации перенаправляет на личный кабинет
LOGIN_REDIRECT_URL = 'profile'
# После выхода из аккаунта перенаправляет на главную
LOGOUT_REDIRECT_URL = 'welcome page'

# DJANGO-ALLAUTH SETTINGS
# Подтверждение регистрации по почте
EMAIL_CONFIRMATION_SIGNUP = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# SMTP GMAIL SETTINGS:
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + "@gmail.com"

# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


CSRF_TRUSTED_ORIGINS = [
    "http://0.0.0.0",
    "http://51.250.69.82",
    "https://51.250.69.82"]
