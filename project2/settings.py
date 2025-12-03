"""
Django settings for django3 project.
Prepared for deployment on Render.
"""

from pathlib import Path
import os
from decouple import config     # pip install python-decouple
import dj_database_url           # pip install dj-database-url

# -------------------------------------------------------------
# BASE DIRECTORY
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------
SECRET_KEY = config("SECRET_KEY", default="django-insecure-change-this")
DEBUG = config("DEBUG", default=False, cast=bool)

# -------------------------------------------------------------
# HOSTS & CSRF
# -------------------------------------------------------------
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Add your custom domain(s) here
ALLOWED_HOSTS += [
    "carbib.onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://carbib.onrender.com",
    f"https://{RENDER_EXTERNAL_HOSTNAME}" if RENDER_EXTERNAL_HOSTNAME else "",
]

# Remove empty strings if RENDER_EXTERNAL_HOSTNAME is missing
CSRF_TRUSTED_ORIGINS = [x for x in CSRF_TRUSTED_ORIGINS if x]

# -------------------------------------------------------------
# AUTH REDIRECTS
# -------------------------------------------------------------
LOGIN_URL = "/login/"
LOGOUT_REDIRECT_URL = "/login/"
LOGIN_REDIRECT_URL = "/myapp/dashboard/"

# -------------------------------------------------------------
# INSTALLED APPS
# -------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your app
    "myapp",
]

# -------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Whitenoise must come RIGHT AFTER SecurityMiddleware
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------------------------------------------
# URLS & WSGI
# -------------------------------------------------------------
ROOT_URLCONF = "django3.urls"
WSGI_APPLICATION = "django3.wsgi.application"  # For Gunicorn / Waitress

# -------------------------------------------------------------
# TEMPLATES
# -------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

# -------------------------------------------------------------
# DATABASE (Render PostgreSQL or SQLite fallback)
# -------------------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False,  # Set True if your DB requires SSL
    )
}

# -------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Kampala"
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------
# STATIC & MEDIA
# -------------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Whitenoise compressed static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------------------------------------------
# DEFAULT PRIMARY KEY
# -------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


