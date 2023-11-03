"""
Django settings for student_residences project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

import os
import environ
import datetime

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

ENVIRONMENT = env("ENVIRONMENT")

# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == "local":
    DEBUG = True


ALLOWED_HOSTS = [
    "sistemaresidenza-staging.herokuapp.com",
    "sistemaresidenza-backend.herokuapp.com",
    "localhost",
]

# Application definition
INSTALLED_APPS = [
    "rest_framework",
    "corsheaders",
    "residence",
    "student",
    "reservation",
    "user",
    "common",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django_filters",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_auth",
    "rest_auth.registration",
    "rest_framework.authtoken",
    "django.contrib.gis",
    "rest_framework_gis",
]


MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = "student_residences.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.normpath(os.path.join(BASE_DIR, "student_residences/templates")),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "user.serializers.NameRegistrationSerializer",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=5),
}

# CONFIGURE S3
AWS_ACCESS_KEY_ID = env("ACCES_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("SECRET_ACCES_KEY")

if ENVIRONMENT != "local":
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_STORAGE_BUCKET_NAME = "sistemaresidenza-bucket"
    AWS_S3_REGION_NAME = "sa-east-1"
    URL_FRONT = "https://residenza-frontend.herokuapp.com/"
    SITE_ID = 6

WSGI_APPLICATION = "student_residences.wsgi.application"

# CONFIGURE DATABASE CONNECTION
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if ENVIRONMENT != "local":
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": env("DATABASE_NAME_PROD"),
            "USER": env("DATABASE_USER_PROD"),
            "PASSWORD": env("DATABASE_PASS_PROD"),
            "HOST": env("DATABASE_HOST_PROD"),
            "PORT": "5432",
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "PORT": "5432",
            "NAME": env("DATABASE_NAME"),
            "USER": env("DATABASE_USER"),
            "PASSWORD": env("POSTGRES_PASS"),
            "HOST": os.environ.get('DATABASE_HOST', 'localhost'),
            "TEST": {
                "NAME": "test_local",
            },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# CONFIGURE TIMEZONE
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Montevideo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

#  Add configuration for static files storage using whitenoise when local environment
if ENVIRONMENT != "local":
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Cors headers configuration
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    "http://localhost",
    "https://sistemaresidenza-backend.herokuapp.com",
    "https://sistemaresidenza-staging.herokuapp.com",
    "https://residenza-frontend.herokuapp.com",
)

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "https://sistemaresidenza-backend.herokuapp.com",
    "https://sistemaresidenza-staging.herokuapp.com",
    "https://residenza-frontend.herokuapp.com",
]
# CORS_ORIGIN_ALLOW_ALL = True
# ALLOWED_HOSTS = ['*']
CSRF_COOKIE_SECURE = True
CORS_ALLOW_CREDENTIALS = True

if ENVIRONMENT == "local":
    URL_FRONT = "http://localhost:3000/"
    SITE_ID = 5

# SCONFIG SENDING EMAILS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = env("MAIL_USER")
EMAIL_HOST_PASSWORD = env("MAIL_KEY")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env("MAIL_USER")
EMAIL_REGISTER = env("EMAIL_REGISTER")

# CONFIG ALLAUTH
LOGIN_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_USERNAME_REQUIRED = False

# same but logged in
if ENVIRONMENT != "local":
    ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = (
        "https://residenza-frontend.herokuapp.com/ingresar"
    )
    ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = (
        "https://residenza-frontend.herokuapp.com/ingresar"
    )
else:
    ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = (
        "http://localhost:3000/ingresar"
    )
    ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "http://localhost:3000/ingresar"
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = True
TEMPLATE_EXTENSION = "email_confirm.html"
