checkNDelete() {
    local path=$1
    if [ -e "$path" ]; then
        echo "Removing: $path"
        if [ $2 ]; then 
            sudo rm -r "$path"
        else
            rm -r "$path"
        fi
    else
        echo "Path does not exist: $path"
    fi
}

checkNDelete ./local/apache.crt false
checkNDelete ./local/apache.key false
checkNDelete ./www/ldap-oauth2/logs true
checkNDelete ./www/ldap-oauth2/staticfiles true
checkNDelete ./www/ldap-oauth2/media true
checkNDelete ./www/ldap-oauth2/db.sqlite3 true

docker-compose down
