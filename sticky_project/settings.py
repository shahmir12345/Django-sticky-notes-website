"""
Django settings for sticky_project.
This file contains the main configuration for the Sticky Notes assignment.
"""
from pathlib import Path

# Base directory of the whole project.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security and debug settings.
SECRET_KEY = 'django-insecure-replace-this-in-production'
DEBUG = True
ALLOWED_HOSTS = []

# Installed applications.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes',  # Custom app for handling sticky notes.
]

# Middleware used by Django for request/response processing.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sticky_project.urls'

# Template configuration.
# DIRS points to the project-level templates folder.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   #Here we add the Template forlder , and we can access Every template folder infact agar kisi bhi Installed app ke folder main jana hai
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sticky_project.wsgi.application'

# SQLite database configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation.
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files configuration.
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Redirect rules required in the assignment Requirements.
LOGIN_REDIRECT_URL = '/notes/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
