#!/bin/sh
docker-compose up --no-deps flyway && \
  docker-compose up --no-deps webserver