#!/usr/bin/env bash

# parameters for the username, image name, tag name, and which directory the Dockerfile lives
userName=$1
imageName=$2
tagName=$3
DockerFileDirectory=$4

# build the image

docker build -t ${userName}/${imageName}:${tagName} ${DockerFileDirectory}