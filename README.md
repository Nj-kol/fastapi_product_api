# Products CRUD API using Fast API

A simple demonstration of creating APIs using the FastAPI library

# Setup

## Create environment

* Checkout the project from git, and under the root folder create a file called `.env`

* Add the following lines :

```bash
PROJECT_NAME=product_api_fastapi
BACKEND_CORS_ORIGINS=["http://localhost:8000", "https://localhost:8000", "http://localhost", "https://localhost"]

DATABASE_URI = 'mysql+pymysql://<db_user>:<db_pass>@<hostname>:<port>/<db_name>'
```

## DB Set up

* Create a table :

```sql
CREATE TABLE product (
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(100),
	description VARCHAR(200),
	price FLOAT,
	qty INTEGER,
	PRIMARY KEY (id),
	UNIQUE (name)
);
```

* Insert some dummy records for testingß

## Run the app

```bash
cd product_api_fastapi
fastapi run
```

# Generated Open API docs

http://127.0.0.1:8000/docs

* Also, an alternate form of API documentation is generated
  
http://127.0.0.1:8000/redoc

# Endpoints

curl http://127.0.0.1:8000/product | jq

**Sample response**

```json
[
  {
    "description": "Biscuit",
    "qty": 1,
    "price": 10,
    "name": "Good Day ",
    "id": 1
  },
  {
    "description": "Shampoo",
    "qty": 1,
    "price": 76,
    "name": "Clinic Plus ",
    "id": 2
  },
  {
    "description": "Coke",
    "qty": 1,
    "price": 20,
    "name": "Coca Cola Classic",
    "id": 3
  }
]
```

# Docker 

```
// Build docker image
docker build -t fastapi_product_api .

// Launch a container
docker run -p 8000:8000 -d \
--name my_container_fastapi \
fastapi_product_api

// Housekeeping
docker logs my_container_fastapi
docker exec -it my_container_fastapi bash

// Teardown
docker container stop my_container_fastapi
docker container rm my_container_fastapi

docker image rm fastapi_product_api
```

# Deploy on Kubernetes

```
kubectl apply -f deploy/

// Use
http://127.0.0.1:30274/docs

// Housekeeping
kubectl get po -o wide
kubectl logs fastapi-product-api-59857c865c-lqxzr -f
kubectl exec -it fastapi-product-api-59857c865c-9g2j2 bash
kubectl get deploy
kubectl get svc

// Teardown
kubectl delete -f deploy/
````