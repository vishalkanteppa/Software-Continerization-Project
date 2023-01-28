#!/bin/sh
docker build -t rest-api:latest rest-api
docker tag rest-api:latest localhost:5000/scproj/rest-api:latest
docker image push localhost:5000/scproj/rest-api:latest
