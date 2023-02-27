# library_layers

POC to run the same code but using multiple python and django versions (another libraries too)

## Project structure

|- root/
|- - core/
|- - - __init__.py
|- - - settings.py
|- - - settings_app.py
|- - - settings_local.py
|- - - urls.py
|- - library_layers/
|- - - layers1_2_7/ # Libraries configured to django-1.2.7
|- - - - libraries/
|- - - - - __init__.py
|- - - - - django/
|- - - - - - __init__.py
|- - - - - - functions.py
|- - - - - - patterns.py
|- - - layers1_11/ # Libraries configured to django-1.11
|- - - - libraries/
|- - - - - __init__.py
|- - - - - django/
|- - - - - - __init__.py
|- - - - - - functions.py
|- - - - - - patterns.py
|- - - layers2_0_13/ # Libraries configured to django-2.0.13
|- - - - libraries/
|- - - - - __init__.py
|- - - - - django/
|- - - - - - __init__.py
|- - - - - - functions.py
|- - - - - - patterns.py
|- - - __init__.py
|- - - loaders.py
|- - - exceptions.py
|- - .dockerignore
|- - .env
|- - .gitignore
|- - __init__.py
|- - docker-compose.2_7_18.yml
|- - docker-compose.3_6_15.yml 
|- - Dockerfile2_7_18
|- - Dockerfile3_6_15
|- - requirements1_2_7.txt
|- - requirements1_11.txt
|- - requirements2_0_13.txt
|- - db127.sqlite3
|- - LICENSE
|- - README.md


## First POC


* Python2.7 with Django-1.2
* Python2.7 with Django-1.11
* Python3.6 with Django-2.0.13
* Python3.6 with Django-3.2
* Python3.10 with Django-4

**NOTE:** In all Django versions the "." was replaced by "_"

## Example

In the manage.py replace the code generated for all django versions and inclue these code in a same function called load_manager and replace the code in the manage.py,  the code must be uncoupled from the business logic and the libraries installed.

```
# manage.py

#!/usr/bin/env python
from library_layers.libraries.django.functions import load_manager

settings, execute_manager = load_manager(file=__file__)


if __name__ == "__main__":
    execute_manager(settings)
```

See load_manager function for Django 1.2.7

```
# library_layers/layers1_2_7/libraries/django/functions.py

def load_manager(*args, **kwargs):
    """
    layer function to translate the default execute manager
    """
    import sys
    from django.core.management import execute_manager

    try:
        file = kwargs.get('file', __file__)
        from core import settings
        return settings, execute_manager
    except ImportError:
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. If appears you've customized things.\nYou'll have to run django-admin.py passing it your seetings module.\n(If the file settings.py does indeed exists, it's causing an ImportError somehow.)\n" % file)
        sys.exit(1)
```

See load_manager function for Django 1.11

```
def load_manager(*args, **kwargs):
    """
    layer function to translate the default execute manager
    """
    import os
    import sys

    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
        from django.core.management import execute_from_command_line
        return sys.argv, execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError("Couldn't import Django. Are you sure its installed and "
                              "available on your PYTHONPATH environment variable? Did you "
                              "forget to activate a virtual environment?")
        raise
```

See load_manager function for Django 2.0.13 (same code used in Django 1.11)

```
def load_manager(*args, **kwargs):
    """
    layer function to translate the default execute manager
    """
    import os
    import sys

    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
        from django.core.management import execute_from_command_line
        return sys.argv, execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError("Couldn't import Django. Are you sure its installed and "
                              "available on your PYTHONPATH environment variable? Did you "
                              "forget to activate a virtual environment?")
        raise
```

## Run Python 2.7 with Django 1.2.7

Change the DJANGO_VERSION in the .env file:

```
# .env file
DJANGO_VERSION=1_2_7
```

Run command:

```
docker compose -f docker-compose.2_7_18.yml down && docker compose -f docker-compose.2_7_18.yml up -d --build
```

Run logs:

```
docker compose -f docker-compose.2_7_18.yml logs
```

Stop or kill the process

```
docker compose -f docker-compose.2_7_18.yml down
```


## Run Python 2.7 with Django 1.11

Change the DJANGO_VERSION in the .env file:

```
# .env file
DJANGO_VERSION=1_11
```

Run command:

```
docker compose -f docker-compose.2_7_18.yml down && docker compose -f docker-compose.2_7_18.yml up -d --build
```

Run Logs:

```
docker compose -f docker-compose.2_7_18.yml logs
```

Stop or kill the process

```
docker compose -f docker-compose.2_7_18.yml down
```

## Run Python 3.6.15 with Django 2.0.13

Change the DJANGO_VERSION in the .env file:

```
# .env file
DJANGO_VERSION=2_0_13
```

Run docker compose commands:

```
docker compose -f docker-compose.3.6.15.yml down && docker compose -f docker-compose.3.6.15.yml up -d --build
```

Run Logs:

```
docker compose -f docker-compose.3.6.15.yml logs
```

Stop or kill the process:

```
docker compose -f docker-compose.3.6.15.yml down
```


Releases
- 1.0 - POC for Django 1.2.7, 1.11 and 2.0.13 only in manage.py, main urls.py and global url patterns.


