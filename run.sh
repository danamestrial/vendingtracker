#!/bin/bash

# If no args, return usage
if [ $# -lt 1 ]; then
	echo "Usage: ./run.sh [frontend | backend | both | server | stop | doctor]"
	exit
fi

if [ $1 == "frontend" ] || [ $1 == "both" ]; then
    echo "Starting frontend"
    tmux new-session -d -s frontend

    #start frontend
    tmux send-keys -t frontend "cd frontend/client" C-m  && \
    tmux send-keys -t frontend "npm install && npm run serve" C-m
fi

if [ $1 == "backend" ] || [ $1 == "both" ]; then
    echo "Starting backend"
    tmux new-session -d -s backend

    #start backend
    tmux send-keys -t backend "poetry install && poetry run flask --app backend/app run" C-m
fi

if [ $1 == "server" ]; then
    echo "Creating test server"
    echo "note: this is a test server, do not use this for deployment"
    echo "creating env file"
    echo "HOST=127.0.0.1
USERNAME=root
PASSWORD=mypassword
DB=vending" > backend/.env
    ./backend/scripts/create-server.sh mypassword
fi

if [ $1 == "stop" ]; then
    echo "Shooting down all process"
    tmux kill-server
fi

if [ $1 == "doctor" ]; then
    COUNT=0
    if ! command -v npm &> /dev/null
    then
        echo "[X] npm"
    else
        echo "[/] npm"
        ((COUNT++))
    fi
    if ! command -v tmux &> /dev/null
    then
        echo "[X] tmux"
    else
        echo "[/] tmux"
        ((COUNT++))
    fi
    if ! command -v python3 &> /dev/null
    then
        echo "[X] python3"
    else
        echo "[/] python3"
        ((COUNT++))
    fi
    if ! command -v poetry &> /dev/null
    then
        echo "[X] poetry"
    else
        echo "[/] poetry"
        ((COUNT++))
    fi
    if ! command -v docker &> /dev/null
    then
        echo "[X] docker"
    else
        echo "[/] docker"
        ((COUNT++))
    fi
    if [ $COUNT == 5 ];
    then
        echo "Everything is set and ready to go!"
    else
        echo "Missing package -> [X]"
    fi
fi
