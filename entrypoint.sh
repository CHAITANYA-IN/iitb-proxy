#!/bin/bash

if [ ! -d "/var/www/ldap-oauth2/logs" ]; then 
    mkdir "/var/www/ldap-oauth2/logs";
fi

if [ -n "$(python /var/www/ldap-oauth2/manage.py collectstatic --dry-run --no-input 2>&1)" ]; then
    python /var/www/ldap-oauth2/manage.py collectstatic --no-input
    cp -R /var/www/ldap-oauth2/static /var/www/ldap-oauth2/staticfiles
fi

if [ ! -f "/var/www/ldap-oauth2/db.sqlite3" ]; then
    touch /var/www/ldap-oauth2/db.sqlite3
    chmod 777 /var/www/ldap-oauth2/db.sqlite3
fi

python /var/www/ldap-oauth2/manage.py makemigrations
python /var/www/ldap-oauth2/manage.py migrate

chmod -R 777 /var/www

exec "$@"
