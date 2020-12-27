# Products CRUD API using Fast API

A simple demonstration of creating APIs using the FastAPI library

## Create project structure

```bash
fastapi startproject \
fastapi_product_api \
--python=3.6 \
--docker \
--database Postgres \
--pre-commit
```

## Run the app

```bash
cd product_api_fastapi
fastapi run
```

**Generated documentation**

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

**Endpoints**

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
