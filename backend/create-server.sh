#!/bin/bash

docker run --name mysql-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mypassword -d mysql