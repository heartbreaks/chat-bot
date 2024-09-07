# README #

### Description ###

* Telegram bot 

### Requirements ###

* docker (https://docs.docker.com/get-docker/)
* docker-compose (https://docs.docker.com/compose/install/linux/)


### Start application ###

First, you need to configure your .env file by template:

    cp .env.local .env

Insert your bot token in .env.

Insert your ingredients in data.json

Then you can simply start service with docker compose:

    docker-compose -f docker/docker-compose-local.yml up -d --build