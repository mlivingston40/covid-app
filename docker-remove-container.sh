#!/usr/bin/env bash

containerId=$1

# You can download and run the image directly in one go using docker run as follows.
# docker run -d dockersamples/static-site-2.1

# See all containers running
# docker ps

# Stop container
docker stop ${containerId}

# Remove container
docker rm ${containerId}

