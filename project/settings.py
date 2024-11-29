import os
from environs import Env

env = Env()
env.read_env()
DATABASES = {
    'default': {
        'DB_ENGINE': env.str("DB_ENGINE"),
        'DB_HOST': env.str("DB_HOST"),
        'DB_PORT': env.int("DB_PORT"),
        'DB_NAME': env.str("DB_NAME"),
        'DB_USER': env.str("DB_USER"),
        'DB_PASSWORD': env.str("DB_PASSWORD")
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str("DB_SECRET_KEY")

DEBUG = env.bool("DB_DEBUG")

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
