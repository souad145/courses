"""
Django settings for campus_management project.
Configuration prête pour Render (production) et fonctionnelle en local (dev).
"""

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# ==================== SECURITY & ENVIRONMENT ====================

# Clé secrète : en production prise depuis les variables d'environnement Render
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-3*+*6p17t@$b_=%-!!_x4*f18w%11v)#mp@y-g%y16oyf+au#&'  # fallback local uniquement
)

# DEBUG : désactivé automatiquement sur Render
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts autorisés : Render fournit RENDER_EXTERNAL_HOSTNAME
ALLOWED_HOSTS = []
if os.environ.get('RENDER'):
    ALLOWED_HOSTS.append(os.environ.get('RENDER_EXTERNAL_HOSTNAME'))
ALLOWED_HOSTS.extend(['localhost', '127.0.0.1', '.onrender.com'])

# ==================== APPLICATION DEFINITION ====================

INSTALLED_APPS = [
    # Prometheus (optionnel mais fortement recommandé pour le TP)
    # 'django_prometheus',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',
    'corsheaders',

    'courses',
    'chatbot',
]

MIDDLEWARE = [
    # Prometheus middleware (décommenter si django_prometheus installé)
    # 'django_prometheus.middleware.PrometheusBeforeMiddleware',

    'corsheaders.middleware.CorsMiddleware',        # Toujours en premier
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # Gestion static files en prod
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'campus_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'campus_management.wsgi.application'
ASGI_APPLICATION = 'campus_management.asgi.application'

# ==================== DATABASE ====================

# Sur Render : utilisation de DATABASE_URL fourni automatiquement par la DB liée
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:Tasnime25@localhost:5432/campus_db',
        conn_max_age=600,
        ssl_require=not DEBUG  # SSL obligatoire en prod
    )
}

# ==================== PASSWORD VALIDATION ====================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==================== INTERNATIONALIZATION ====================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==================== STATIC FILES (CSS, JavaScript, Images) ====================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==================== DEFAULT PRIMARY KEY ====================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================== DRF CONFIG ====================

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',   # Attention en prod : à restreindre plus tard
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ],
}

# ==================== CORS ====================

# En dev : tout autorisé
# En prod : à restreindre fortement (ex: ton frontend uniquement)
CORS_ALLOW_ALL_ORIGINS = DEBUG
if not DEBUG:
    CORS_ALLOWED_ORIGINS = [
        # Ajoute ici ton frontend en prod, ex:
        # "https://mon-frontend.net",
    ]

# ==================== LOGGING (optionnel mais utile sur Render) ====================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}