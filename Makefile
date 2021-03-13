PROJECT_NAME=hackernews

all: start

start:
	@docker-compose up --force-recreate --build --detach

stop:
	@docker-compose stop
	@docker-compose down

bash:
	@docker exec -it hackernews bash

logs:
	@docker logs -f hackernews

ping:
	@echo curl "http://localhost/ping"
	@curl "http://localhost/ping"

restart:
	@docker-compose stop
	@docker-compose up

mysql:
	@docker exec -it hackernews_mysql -u user -p