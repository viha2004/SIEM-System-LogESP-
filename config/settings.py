# LogESP secondary settings file

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v2oem$sm5mtfz4n8=t)c37&y^3=c+)jxl2hf3ws$7(#eevpw+)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Email settings
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.example.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'logespserver@example.com'
#EMAIL_HOST_PASSWORD = 'BIGSECRET'
#EMAIL_ALERT_FROM_ADDRESS = 'noreply@example.com'
#DEFAULT_FROM_EMAIL = 'noreply@example.com'
#SERVER_EMAIL = 'noreply@example.com'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Etc/UTC'
