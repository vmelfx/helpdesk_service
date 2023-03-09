#!/bin/bash

cd ~/helpdesk_service/

git pull origin main
docker-compose down && docker-compose up --build -d