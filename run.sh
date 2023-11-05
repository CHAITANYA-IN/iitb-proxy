#!/bin/sh

# Set these variables manually
export OIDC_CLIENT_ID=""
export OIDC_CLIENT_SECRET=""
export OIDC_CRYPTO_PASSPHRASE=""

envsubst < demo_site_template.conf > demo_site.conf

unset OIDC_CLIENT_ID
unset OIDC_CLIENT_SECRET
unset OIDC_CRYPTO_PASSPHRASE

sudo docker compose up --build
