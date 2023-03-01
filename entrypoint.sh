#!/bin/sh

sleep 2s
MEDIA_DIR=/usr/local/lib/python2.7/site-packages/django/contrib/admin/media
TEMPLATES_DIR=/usr/local/lib/python2.7/site-packages/django/contrib/admin/templates

if [ -d "${MEDIA_DIR}" ]; then
  echo "The dir '${MEDIA_DIR}' already exists..."
else

  if [ -d "/usr/local/django/contrib/admin/media" ]; then
    echo "Copying files to '${MEDIA_DIR}'..."
    cp -rf /usr/local/django/contrib/admin/media /usr/local/lib/python2.7/site-packages/django/contrib/admin
    echo "The dir '${MEDIA_DIR}' has been adjusted."
  fi
fi

if [ -d "${TEMPLATES_DIR}" ]; then
  echo "The dir '${TEMPLATES_DIR}' already exists..."
else
  echo "Copying files to '${TEMPLATES_DIR}'..."
  cp -rf /usr/local/django/contrib/admin/templates /usr/local/lib/python2.7/site-packages/django/contrib/admin
  echo "The dir '${TEMPLATES_DIR}' has been adjusted."
fi

python manage.py runserver 0.0.0.0:8000
echo "Application already started!"
exec "$@"
