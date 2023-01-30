# Software-Continerization-Project

## Creating local docker registry (for development???)
```bash
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

Note that for production we would probably want to use a different registry than localhost. (TODO WHY ? SPECIFY MORE ETC . DONT EVEN KNOW IF THIS IS BEST PRACTICE)


## Build docker images
```bash
docker build -t rest-api:latest rest-api
```

## Tag and push locally
```bash
docker tag rest-api:latest localhost:5000/scproj/rest-api:latest
docker image push localhost:5000/scproj/rest-api:latest
```

## Build and run frontend
```
docker build -t frontend:latest frontend
docker run -d -p 5001:5000 --restart=always --name frontend-container frontend:latest
```

## Kubectl apply 
```bash
kubectl apply -f k8s-specifications/
```

## Show pods
```bash
kubectl get pods
```

## Delete
```bash
kubectl delete -f k8s-specifications/
```
