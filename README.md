create a new file named as "local_settings.py" and add this information According to yours configurations
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "",
        'USER': "",
        'PASSWORD': "",
        'HOST': "",
        'PORT': "",
    }
}

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''