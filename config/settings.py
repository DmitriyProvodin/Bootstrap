import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY','replace-me')
DEBUG = os.getenv('DEBUG','True') == 'True'
INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','rest_framework','rest_framework_simplejwt.token_blacklist','django_filters','drf_spectacular','django_celery_beat','users','courses']
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF = 'config.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'config.wsgi.application'
DATABASES = {'default':{'ENGINE':'django.db.backends.postgresql','NAME': os.getenv('DB_NAME','lms_db'),'USER': os.getenv('DB_USER','postgres'),'PASSWORD': os.getenv('DB_PASSWORD','postgres'),'HOST': os.getenv('DB_HOST','localhost'),'PORT': os.getenv('DB_PORT','5432'),}}
AUTH_USER_MODEL = 'users.User'
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework_simplejwt.authentication.JWTAuthentication',),'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',),'DEFAULT_FILTER_BACKENDS':('django_filters.rest_framework.DjangoFilterBackend','rest_framework.filters.OrderingFilter',),'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',}
SIMPLE_JWT = {'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),'REFRESH_TOKEN_LIFETIME': timedelta(days=1)}
SPECTACULAR_SETTINGS = {'TITLE':'LMS API','VERSION':'1.0.0'}
CELERY_BROKER_URL = os.getenv('REDIS_URL','redis://localhost:6379/0')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_TIMEZONE = os.getenv('TIME_ZONE','UTC')
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY','')
