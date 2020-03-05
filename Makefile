help:
	@echo "Welcome to the Telemetry Airflow\n"
	@echo "The list of commands for local development:\n"
	@echo "  build      Builds the docker images for the docker-compose setup"
	@echo "  clean      Stops and removes all docker containers"
	@echo "  migrate    Runs the Django database migrations"
	@echo "  redis-cli  Opens a Redis CLI"
	@echo "  run        Run a airflow command"
	@echo "  secret     Create a secret to be used for a config variable"
	@echo "  shell      Opens a Bash shell"
	@echo "  up         Runs the whole stack, served under http://localhost:8000/\n"
	@echo "  stop       Stops the docker containers"

build:
	docker-compose build

clean: stop
	docker-compose rm -f
	docker volume rm $(docker volume ls -qf dangling=true)

shell:
	docker-compose run web bash

up: build
	docker-compose down
	docker-compose up

stop:
	docker-compose down
	docker-compose stop