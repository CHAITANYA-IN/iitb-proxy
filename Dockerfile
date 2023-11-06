FROM ubuntu

#RUN RUN chown -R www-data:www-data
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
#RUN apt install -y software-properties-common
#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python3.9
RUN apt-get -y install python3
RUN apt-get -y install libapache2-mod-wsgi-py3

RUN ln /usr/bin/python3 /usr/bin/python
#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#RUN apt install -y python3.9-distutils
#RUN python3.9 get-pip.py
#RUN apt-get install -y python-venv
RUN apt-get install -y apache2-dev
ADD ./www/ldap-oauth2/requirements.txt /tmp/env.txt
#RUN apt-get -y install python3-pip
#RUN ln -sf usr/bin/pip3 /usr/bin/pip
#RUN pip install --upgrade pip
RUN apt-get -y install python3-pip
#RUN pip install virtualenv
#RUN python -m venv venv
#RUN virtualenv venv
RUN  pip install django
#RUN venv/bin/activate
RUN pip install -r /tmp/env.txt
RUN pip install ptvsd
RUN pip install https://github.com/GrahamDumpleton/mod_wsgi/archive/develop.zip

RUN mkdir -p /var/log/django
RUN mkdir -p /opt/
#RUN cp -r venv ~/
RUN apt-get install -y libapache2-mod-auth-openidc
RUN a2enmod auth_openidc
ADD ./demo_site.conf /etc/apache2/sites-available/000-default.conf
RUN apt-get install apache2 openssl
RUN a2enmod ssl
RUN a2enmod rewrite
#RUN service apache2 restart
RUN mkdir /etc/apache2/certs
ADD ./apache.crt /etc/apache2/certs/apache.crt
ADD ./apache.key /etc/apache2/certs/apache.key
#RUN chown -R www-data:www-data /var/www
USER root
RUN chmod -R 777 /var/www
EXPOSE 80 3500 443
CMD ["apache2ctl", "-D", "FOREGROUND"]
