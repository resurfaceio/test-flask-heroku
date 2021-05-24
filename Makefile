PROJECT_NAME=hackernews

start:
	@docker stop resurface || true
	@docker build -t test-flask-hackernews --no-cache .
	@docker-compose up --detach

stop:
	@docker-compose stop
	@docker-compose down --volumes
	@docker image rmi -f test-flask-hackernews

bash:
	@docker exec -it hackernews bash

logs:
	@docker logs -f hackernews

ping:
	@curl "http://localhost/ping"

restart:
	@docker-compose stop
	@docker-compose up
