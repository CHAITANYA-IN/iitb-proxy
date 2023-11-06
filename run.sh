#!/bin/sh

# Generate Apache key and certificate
if [ ! -f ./apache.key ] || [ ! -f ./apache.crt ]; then
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout apache.key -out apache.crt -subj "/C=IN/ST=MH/L=Powai/O=IIT Bombay/CN=cse.iitb.ac.in"
fi

# Set these variables manually
export OIDC_CLIENT_ID=""
export OIDC_CLIENT_SECRET=""
export OIDC_CRYPTO_PASSPHRASE=""

# Substitute the variables in the template
envsubst < demo_site_template.conf > demo_site.conf

# Unset the variables
unset OIDC_CLIENT_ID
unset OIDC_CLIENT_SECRET
unset OIDC_CRYPTO_PASSPHRASE

# Run the Docker container
sudo docker compose up --build
