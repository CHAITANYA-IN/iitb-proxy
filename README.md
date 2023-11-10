# SSO Proxy Server

## Run the project

### Pre-requisites

#### Set the environment variables

Create a directory `local` and `.env` file inside

```sh
mkdir ./local
touch ./local/.env
```

.env file should set the following variables:

```sh
OIDC_CLIENT_ID=""
OIDC_CLIENT_SECRET=""
OIDC_CRYPTO_PASSPHRASE=""
LDAP_SESSION_CRYPTO_PASSPHRASE=""
SECRET_KEY=""
APACHE_CERTIFICATE_SIGNING_REQUEST_SUBJECT=""
```

Make sure *.sh files have executable permission, use the following command to give them executable permission

```sh
chmod +x *.sh
```

### Start the project

```sh
./run.sh
```

> If you want to run the docker containers in detach mode,
> Add `-d` option to the docker-compose command in `run.sh`

To clean the production files and directories, run

```sh
./clean.sh
```

## Developer

### Information on dockerizing apache + django project

This is a docker project to create a container with Python3, Django and Apache2. All configurations, along with a sample django project are cerated.

* docker-compose up

    Starts the container named django-apache2
* Browse to http://localhost:8500

    A sample employee list page is displayed.

See Dockerfile and docker-compose.yml for configuration details.

See [blog post](http://ramkulkarni.com/blog/docker-project-for-python3-djaongo-and-apache2-setup/) and [this video](https://youtu.be/OtZmCBR7J-k)
