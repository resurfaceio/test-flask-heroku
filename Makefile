PROJECT_NAME=hackernews

start:
	@docker stop resurface || true
	@docker build -t test-flask --no-cache .
	@docker-compose up --detach

stop:
	@docker-compose stop
	@docker-compose down --volumes
	@docker image rmi -f test-flask

bash:
	@docker exec -it flask bash

logs:
	@docker logs -f flask

ping:
	#todo switch to GraphQL post
	@curl "http://localhost/ping"

restart:
	@docker-compose stop
	@docker-compose up --detach

test:
	@docker exec -it flask python3 test.py