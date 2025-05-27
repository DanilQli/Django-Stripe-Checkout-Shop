import os
from pathlib import Path
from decouple import config

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*']  # Для локального запуска и PythonAnywhere
# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payments.apps.PaymentsConfig',  # Подключение основного приложения
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основной URL-конфиг
ROOT_URLCONF = 'stripe_project.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'payments' / 'templates'],
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

WSGI_APPLICATION = 'stripe_project.wsgi.application'

# База данных: SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Пароли
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# Язык / Время
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Путь к статике
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

STRIPE_SECRET_KEY_USD = config('STRIPE_SECRET_KEY_USD')
STRIPE_PUBLISHABLE_KEY_USD = config('STRIPE_PUBLISHABLE_KEY_USD')
STRIPE_SECRET_KEY_EUR = config('STRIPE_SECRET_KEY_EUR')
STRIPE_PUBLISHABLE_KEY_EUR = config('STRIPE_PUBLISHABLE_KEY_EUR')
DEFAULT_CURRENCY = config('DEFAULT_CURRENCY', default='usd')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
