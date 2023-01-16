# Vending Tracker
A ICCS372 Homework

----

## Run Requirement
>### Frontend (Vue)
<mark>Required:</mark> npm

>### Backend (Flask)
<mark>Required:</mark> python3, poetry

>### Database (MySql on Docker)
<mark>Required:</mark> docker

>### Deploy Script
<mark>Required:</mark> npm, python3, poetry, tmux

## Run using script
`chmod +x ./deploy.sh` \
`./deploy.sh [ backend | frontend | both | stop | doctor ]`

If you are not sure which packages are already installed run `./deploy.sh doctor`

## Running it manually
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

