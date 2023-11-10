rm local/apache.crt
rm local/apache.key
sudo rm -r ./www/ldap-oauth2/logs
sudo rm -r ./www/ldap-oauth2/staticfiles
sudo rm -r ./www/ldap-oauth2/media
sudo rm -r ./www/ldap-oauth2/db.sqlite3
docker-compose down
