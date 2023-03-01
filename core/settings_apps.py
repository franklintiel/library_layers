DJANGO_APPS = DJANGO_APPS + [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',    
]

THIRD_PARTY_APPS = THIRD_PARTY_APPS + list()

CUSTOM_APPS = list()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
