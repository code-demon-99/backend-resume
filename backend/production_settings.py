from .settings import *
import os 
import django_heroku
DEBUG=False

ALLOWED_HOSTS += ['myownresume.herokuapp.com']
INSTALLED_APPS += [
    
    'rest_framework',
    'rest_framework_swagger',
    
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MIDDLEWARE+=[
   'whitenoise.middleware.WhiteNoiseMiddleware',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoS   chema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfuugc05oagmub',
        'HOST': 'ec2-34-230-198-12.compute-1.amazonaws.com',
        'USER': 'tiwqjyozmiifqu',
        'PORT': 5432,
        'PASSWORD': 'e91d8335dcedca26d8cbf126dc6c3d6a1ad3c97dd11c29227295081f88357d4f'
        
    }
}

CORS_ALLOWED_ORIGINS = [
    "https://www.rishinamdev.ml",
    "http://localhost:4200"

]
CORS_URLS_REGEX = r"^/api/.*$"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

django_heroku.settings(locals())