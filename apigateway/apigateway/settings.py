import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def str_to_bool(value):
    """ Converts a string to a boolean. """
    return str(value).lower() in ("true", "1", "yes")

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret')
DEBUG = str_to_bool(os.environ.get('DEBUG', 'false'))

# Updated ALLOWED_HOSTS logic to handle '*'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'src.middleware.JWTAuthenticationMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

EXCLUDED_ROUTES = [
    '/user/login', '/user/register', '/user/2fa', '/user/pwd/forgot',
    '/auth/intra', '/auth/intra/callback', '/auth/token/validate', '/auth/token/refresh',
    '/user/oauth/create', '/user/email_verify', '/user/reset-password',
    '/user/pwd/change', '/user/image', '/user/image/serve', '/favicon.ico'
]

SERVICE_ROUTES = {
    '/auth': 'http://authservice:8001',
    '/friends': 'http://friendservice:8012',
    '/game': 'http://gameservice:8010',
    '/user': 'http://usermanagement:8004',
}

ROOT_URLCONF = 'apigateway.urls'

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

WSGI_APPLICATION = 'apigateway.wsgi.application'

STATIC_URL = '/static/'
