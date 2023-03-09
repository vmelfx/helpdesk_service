import os
from distutils.util import strtobool
from os import getenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
SRC_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_DIR = SRC_DIR.parent

SECRET_KEY = getenv("DJANGO_SECRET_KEY", default="INVALID")
DEBUG = strtobool(getenv("DJANGO_DEBUG", default="0"))
ALLOWED_HOSTS = getenv("DJANGO_ALLOWED_HOSTS", default="").split(",")


# Set custom user model
AUTH_USER_MODEL = "users.User"

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_yasg",
]

LOCAL_APPS = [
    "exchange_rates",
    "users",
    "tickets",
    "comments",
    "shared",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": getenv("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": getenv("DB_NAME", default="support"),
        "USER": getenv("DB_USER", default="postgres"),
        "PASSWORD": getenv("DB_PASSWORD", default="postgres"),
        "HOST": getenv("DB_HOST", default="postgres"),
        "PORT": getenv("DB_PORT", default=5432),
    }
}

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

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

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# STATIC_ROOT = ROOT_DIR / "staticfiles"
# STATIC_URL = "/static/"
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")


CSRF_TRUSTED_ORIGINS = getenv("CSRF_TRUSTED_ORIGINS", default="").split(",")  # type: ignore
