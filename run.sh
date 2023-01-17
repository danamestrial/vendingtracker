#!/bin/bash

# If no args, return usage
if [ $# -lt 1 ]; then
	echo "Usage: ./run.sh [frontend | backend | both | stop | doctor]"
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
    tmux send-keys -t backend "cd backend" C-m && \
    tmux send-keys -t backend "poetry install && poetry run python3 app.py" C-m
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
    if [ $COUNT == 4 ];
    then
        echo "Everything is set and ready to go!"
    else
        echo "Missing package -> [X]"
    fi
fi
