#!/bin/sh
docker build -t rest-api:latest rest-api
docker tag rest-api:latest localhost:5000/scproj/rest-api:latest
docker image push localhost:5000/scproj/rest-api:latest

docker build -t frontend:latest frontend
docker tag frontend:latest localhost:5001/scproj/frontend:latest
docker image push localhost:5001/scproj/frontend:latest
