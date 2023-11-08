from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-huieg#*g=u@=l-jkm$aic+=_2+my0e7lfo8q(_!&7h3+-#7ydv'

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "g1product",
        'USER': "root",
        'PASSWORD': "root",
        'HOST': "localhost",
        'PORT': "3306",
    }
}

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ahsananees709@gmail.com'
EMAIL_HOST_PASSWORD = 'duoahkcfbvzntudk'
