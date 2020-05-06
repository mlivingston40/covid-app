#!/usr/bin/env bash

imageName=$1
author=$2
tagName=$3
containerName=$4

echo Actually runs locally on http://localhost:8888

docker run -p 8888:5000 --name ${containerName} ${author}/${imageName}:${tagName}

