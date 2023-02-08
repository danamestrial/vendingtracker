#!/bin/bash

# If no args, return usage
if [ $# -lt 1 ]; then
	echo "Usage: ./create-server.sh {password}"
	exit
fi

COUNTER=0

docker run --name mysql-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=$1 -d mysql
while ! docker exec -i mysql-db mysql --user=root --password=$1 -e "status" &> /dev/null ; do
    echo "Waiting for database to start... [$COUNTER]"
    if [ $COUNTER -eq 30 ]; then
      echo "Timed out, cannot exec .sql script in time (database might be too slow to start)"
      exit
    fi
    sleep 2
    let COUNTER++
done
docker exec -i mysql-db mysql -u root -p$1 < ./backend/scripts/create-database-with-data.sql

echo "Server created sucessfully"
