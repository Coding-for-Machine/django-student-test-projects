
import os
from pathlib import Path

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ktc=wxu7vbf-+fa+3x#73x26d(jlf@$#1-wq*c++&sweczdt6w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django_daisy',#hey
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',

    'users.apps.UsersConfig',
    'quizes.apps.QuizesConfig',
    'questions.apps.QuestionsConfig',
    'results.apps.ResultsConfig',
    
]
APPS_REORDER = {
    # django auth app
    'auth': {
        'app': 'users',
        'icon': 'fa fa-tachometer-alt',
        'name': ('Test-Admin'),
        'hide': False,
    },

    # social-auth-app-django app
    'social_django': {
        'icon': 'fa fa-tachometer-alt'
    }
}

AUTH_USER_MODEL = "users.User"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# register
LOGIN_REDIRECT_URL = "quizes:quizlist"
LOGOUT_REDIRECT_URL = "users:login"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# ROOT_DIR = os.path.dirname(BASE_DIR)

STATIC_URL = 'static/'
STATIC_ROOT=BASE_DIR / 'staticfile'

STATICFILES_DIRS =[
    BASE_DIR / "static"
]

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
from django.contrib.messages import constants as message

MESSAGE_TAGS = {
     message.DEBUG: 'text-yellow', 
     message.INFO: 'text-green',
     message.SUCCESS: 'text-green',
     message.WARNING: 'text-yellow',
     message.ERROR: 'text-red',
}
