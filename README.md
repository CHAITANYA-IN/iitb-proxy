# SSO Proxy Server

## Run the project

Create a .env file defining following variables:

```sh
OIDC_CLIENT_ID=""
OIDC_CLIENT_SECRET=""
OIDC_CRYPTO_PASSPHRASE=""
LDAP_SESSION_CRYPTO_PASSPHRASE=""
SECRET_KEY=""
APACHE_CERTIFICATE_SIGNING_REQUEST_SUBJECT=""
```

## Docker project for Django and Apache2

This is a docker project to create a container with Python3, Django and Apache2. All configurations, along with a sample django project are cerated.

* docker-compose up

    Starts the container named django-apache2
* Browse to http://localhost:8500

    A sample employee list page is displayed.

See Dockerfile and docker-compose.yml for configuration details.

See [blog post](http://ramkulkarni.com/blog/docker-project-for-python3-djaongo-and-apache2-setup/) and [this video](https://youtu.be/OtZmCBR7J-k)
