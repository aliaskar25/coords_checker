# coords_checker
Test Task using FastAPI, PostgreSQL, Docker and Dependency Injector (DDD)


## How to run application

1. Get api key from https://geocode.maps.co/
2. Create .env file and paste your values as in .env-example 
3. ``` docker-compose -f docker-compose.yml up --build -d ``` add "sudo" if you are on Mac


## To add changes in Tables in DB

1. docker-compose run --rm migrations alembic revision --autogenerate -m "{your message}"
2. docker-compose run --rm migrations alembic upgrade head


### See api docs in /api/docs/ui

## There are several endpoints (esli len' zahodit' v swagger):

1. http://127.0.0.1:8000/api/v1/geopoints/get-by-name
in body paste {"name": "Tash Rabat"}

2. http://127.0.0.1:8000/api/v1/geopoints/get-by-lan-lat
in body paste {"lon": "74.59040758538325", "lat": "42.874486450000006"}
