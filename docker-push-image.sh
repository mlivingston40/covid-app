#!/usr/bin/env bash

imageName=$1
author=$2
tagName=$3

docker login

docker push ${author}/${imageName}:${tagName}