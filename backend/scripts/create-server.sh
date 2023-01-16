#!/bin/bash

# If no args, return usage
if [ $# -lt 1 ]; then
	echo "Usage: ./create-server.sh {password}"
	exit

docker run --name mysql-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=$1 -d mysql