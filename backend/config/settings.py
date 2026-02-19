import os
from pathlib import Path
from datetime import timedelta

# ===============================
# BASE DIRECTORY
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ===============================
# SECURITY
# ===============================
SECRET_KEY = 'django-insecure-9x2@sample$secret!key#2026@airesume'

DEBUG = False

ALLOWED_HOSTS = ['*']  # Later replace with your Render domain


# ===============================
# APPLICATIONS
# ===============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'corsheaders',

    'apps.accounts',
    'apps.resumes',
    'apps.jobs',
    'apps.applications',
    'apps.notifications',
    'apps.analytics',
    'apps.ai_matching.apps.AiMatchingConfig',
]


# ===============================
# MIDDLEWARE
# ===============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ===============================
# TEMPLATES (🔥 REQUIRED FOR ADMIN)
# ===============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # optional folder
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


# ===============================
# URLS & WSGI
# ===============================
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# ===============================
# DATABASE
# ===============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===============================
# STATIC FILES
# ===============================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ⚠ REMOVE STATICFILES_DIRS (caused warning on Render)
# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]


# ===============================
# MEDIA FILES
# ===============================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ===============================
# AUTH
# ===============================
AUTH_USER_MODEL = 'accounts.User'


# ===============================
# DEFAULT PRIMARY KEY FIX
# ===============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ===============================
# REST FRAMEWORK
# ===============================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


# ===============================
# SWAGGER
# ===============================
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}


# ===============================
# CORS
# ===============================
CORS_ALLOW_ALL_ORIGINS = True
