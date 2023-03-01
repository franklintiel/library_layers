DJANGO_VERSION = os.environ.get('DJANGO_VERSION', None)

if not DJANGO_VERSION:
    raise AttributeError("The environment variable DJANGO_VERSION does not exists.")

database_name = 'db{database_name}.sqlite3'.format(database_name=DJANGO_VERSION)
dbname = "{base_dir}/dbs/{database_name}".format(base_dir=BASE_DIR, database_name=database_name)

DATABASES={
    'default': {
        'ENGINE': "django.db.backends.sqlite3",
        'NAME': dbname,
    }
}

ROOT_URLCONF = 'core.urls'
