"""
Django settings for project2 project.
Prepared for deployment on Render.
"""

from pathlib import Path
import os
from decouple import config
import dj_database_url

# 🔹 BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 SECURITY
SECRET_KEY = config('SECRET_KEY', default='django-insecure-please-change-this')
DEBUG = config('DEBUG', default=False, cast=bool)

# 🔹 Hosts and CSRF
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost,carbib.onrender.com').split(',')
CSRF_TRUSTED_ORIGINS = [f'https://{host}' for host in ALLOWED_HOSTS if host not in ['127.0.0.1', 'localhost']]

# 🔹 Authentication Redirects
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_REDIRECT_URL = '/myapp/dashboard/'
LOGIN_URL = '/login/'

# 🔹 Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your app
    'myapp',
]

# 🔹 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔹 URL Configuration
ROOT_URLCONF = 'project2.urls'

# 🔹 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates folder
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

# 🔹 WSGI
WSGI_APPLICATION = 'project2.wsgi.application'

# 🔹 Database (SQLite locally, auto-switches on Render)
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

# 🔹 Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Kampala'
USE_I18N = True
USE_TZ = True

# 🔹 Static and Media Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Local development
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Production

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Whitenoise static files optimization
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 🔹 Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔹 Render-friendly environment variables
# Use a .env file or Render Environment Variables
# Example .env:
# SECRET_KEY=<your secret>
# DEBUG=False
# ALLOWED_HOSTS=carbib.onrender.com
