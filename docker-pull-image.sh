#!/usr/bin/env bash

imageName=$1
author=$2
#tagName=$3

docker pull ${author}/${imageName}

#docker pull ${author}/${imageName}:${tagName}