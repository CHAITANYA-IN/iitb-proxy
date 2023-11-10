#!/bin/sh

ENV_DIR=./local
. ${ENV_DIR}/.env

# Generate Apache key and certificate
if [ ! -f ${ENV_DIR}/apache.key ] || [ ! -f ${ENV_DIR}/apache.crt ]; then
    openssl req -noenc -x509 -newkey rsa:4096 -keyout "${ENV_DIR}/apache.key" -out "${ENV_DIR}/apache.crt" -days 365 -subj "${APACHE_CERTIFICATE_SIGNING_REQUEST_SUBJECT}" --passout "pass:${APACHE_KEY_PASSPHRASE}"
fi

# Run the Docker container
docker-compose up
