# library_layers

POC to run the same code but using multiple python and django versions (another libraries too)

## Project structure

```
|- root/
|-- core/
|--- __init__.py
|--- settings.py
|--- settings_app.py
|--- settings_local.py
|--- urls.py
|-- .dockerignore
|-- .env
|-- .gitignore
|-- __init__.py
|-- docker-compose.2_7_18.yml
|-- docker-compose.3_6_15.yml
|-- Dockerfile2_7_18
|-- Dockerfile3_6_15
|-- requirements1_2_7.txt
|-- requirements1_11.txt
|-- requirements2_0_13.txt
|-- db127.sqlite3
|-- LICENSE
|-- README.md
|-- library_layers/ # this is where the magic happens
|--- layers1_2_7/ # Libraries configured to django-1.2.7
|---- libraries/
|----- __init__.py
|----- django/
|------ __init__.py
|------ functions.py
|------ patterns.py
|------ settings.py
|--- layers1_11/ # Libraries configured to django-1.11
|---- libraries/
|----- __init__.py
|----- django/\
|------ __init__.py
|------ functions.py
|------ patterns.py
|------ settings.py
|--- layers2_0_13/ # Libraries configured to django-2.0.13
|---- libraries/
|----- __init__.py
|----- django/
|------ __init__.py
|------ functions.py
|------ patterns.py
|------ settings.py
|--- __init__.py
|--- layers3_2_18/ # Libraries configured to django-3.2.18
|---- libraries/
|----- __init__.py
|----- django/
|------ __init__.py
|------ functions.py
|------ patterns.py
|------ settings.py
|--- __init__.py
|--- layers4_1_7/ # Libraries configured to django-4.1.7
|---- libraries/
|----- __init__.py
|----- django/
|------ __init__.py
|------ functions.py
|------ patterns.py
|------ settings.py
|--- __init__.py
|--- loaders.py
|--- exceptions.py
```


## First POC


* Python2.7.18 with Django-1.2
* Python2.7.18 with Django-1.11
* Python3.6.15 with Django-2.0.13
* Python3.9.4 with Django-3.2.18
* Python3.9.4 with Django-4.1.7

**NOTE:** In all Django versions the "." was replaced by "_"

## Example

In the manage.py replace the code generated for all django versions and inclue these code in a same function called load_manager and replace the code in the manage.py,  the code must be uncoupled from the business logic and the libraries installed.


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

Syncdb and Run Migrations


```
# access to docker container
docker exec -it django-app sh 

# run the syncdb (for first time)
# Create a user with this credentials:
# username: admin
# email: info@domain.com
# password: admin@1234
python manage.py syncdb 

# Run migrations
python manage.py migrate 
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

Syncdb and Run Migrations

```
#\ access to docker container
docker exec -it django-app sh

# create superuser
# username: admin
# email: info@domain.com
# password: 1234
python manage.py createsuperuser

# Run migrations
python manage.py migrate
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

Syncdb and Run Migrations

```
# access to docker container
docker exec -it django-app sh

# create superuser
# username: admin
# email: info@domain.com
# password: 1234
python manage.py createsuperuser

# Run migrations
python manage.py migrate
```


## Run Python 3.9.4 with Django 3.2.18

Change the DJANGO_VERSION in the .env file:

```
# .env file
DJANGO_VERSION=3_2_18
```

Run docker compose commands:

```
docker compose -f docker-compose.3.9.4.yml down && docker compose -f docker-compose.3.9.4.yml up -d --build
```

Run Logs:

```
docker compose -f docker-compose.3.9.4.yml logs
```

Stop or kill the process:

```
docker compose -f docker-compose.3.9.4.yml down
```

Syncdb and Run Migrations

```
# access to docker container
docker exec -it django-app sh

# create superuser
# username: admin
# email: info@domain.com
# password: 1234
python manage.py createsuperuser

# Run migrations
python manage.py migrate
```


## Run Python 3.9.4 with Django 4.1.7

Change the DJANGO_VERSION in the .env file:

```
# .env file
DJANGO_VERSION=4_1_7
```

Run docker compose commands:

```
docker compose -f docker-compose.3.9.4.yml down && docker compose -f docker-compose.3.9.4.yml up -d --build
```

Run Logs:

```
docker compose -f docker-compose.3.9.4.yml logs
```

Stop or kill the process:

```
docker compose -f docker-compose.3.9.4.yml down
```

Syncdb and Run Migrations

```
# access to docker container
docker exec -it django-app sh

# create superuser
# username: admin
# email: info@domain.com
# password: 1234
python manage.py createsuperuser

# Run migrations
python manage.py migrate
```

# Releases
- 1.0 - POC for Django 1.2.7, 1.11 and 2.0.13 only in manage.py, main urls.py and global url patterns.
- 2.0 - POC for Django 3.2.18 and 4.1.7 only in manage.py, main urls.py and global url patterns.
- 3.0 - Connecting process to do migrations and start the admin section for all django versions


