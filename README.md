[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=danamestrial_vendingtracker&metric=coverage)](https://sonarcloud.io/summary/new_code?id=danamestrial_vendingtracker)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=danamestrial_vendingtracker&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=danamestrial_vendingtracker)

# Vending Tracker
A ICCS372 Homework

----

### Homework Checklist

- [x] Should be able to manage (create edit delete) vending machines (name, location ,etc)
- [x] There are multiple products coke, taro, pringle etc
- [x] There is a stock for each vending machine (api to crud)
- [x] Listing for vending machine stock products etc

## Run Requirement
>### Frontend (Vue)
<mark>Required:</mark> npm

>### Backend (Flask)
<mark>Required:</mark> python3, poetry

>### Database (MySql on Docker)
<mark>Required:</mark> docker

>### Run Script
<mark>Required:</mark> npm, python3, poetry, tmux, docker

## Run using script
`chmod +x ./run.sh` \
usage: ./run.sh [ backend | frontend | both | server | stop | doctor ]

`./run.sh server` -> Create test server (required docker)

`./run.sh backend` -> Start backend (run flask app using tmux)

`./run.sh frontend` -> Start frontend (not updated)

`./run.sh both` -> Start both frontend and backend (not updated)

`./run.sh stop` -> Stop backend/frontend (stop all tmux session)

##### If you are not sure which packages are already installed run:

`./run.sh doctor` -> Check which package is installed

## Create Database using run script


## Running/Creating manually
>### Frontend
`cd frontend/client`\
`npm install`\
`npm run serve`

>### Backend
`cd backend`\
`poetry install`\
`poetry run python3 app.py`

>### Server
`cd backend/scripts`\
`chmod +x ./create-server.sh`\
`./create-server.sh {password}`
