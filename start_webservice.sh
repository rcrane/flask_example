#!/bin/bash

docker build -t webflask .
docker run -v $(pwd):/project --workdir="/project" webflask:latest python3 webservice.py