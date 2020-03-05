#!/usr/bin/env bash

#set -eo pipefail
#set -x
# export all modified varibles
set -o allexport

# default variables
: "${PORT:=8000}"
: "${SLEEP:=1}"
: "${TRIES:=60}"
: "${AIRFLOW__CORE__EXECUTOR:="CeleryExecutor"}"

usage() {
  echo "usage: bin/run flower|web|worker|scheduler"
  exit 1
}

wait_for() {
  tries=0
  echo "Waiting for $1 to listen on $2..."
  while true; do
    [[ $tries -lt $TRIES ]] || return
    (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
    result=
    [[ $? -eq 0 ]] && return
    sleep $SLEEP
    tries=$((tries + 1))
  done
}

# Setup Worker Credentials
: "${WORKER_PASS:=worker}"

# Setup postgres database connection
: "${POSTGRES_HOST:="db"}"
: "${POSTGRES_PORT:="5432"}"
: "${POSTGRES_USER:="airflow"}"
: "${POSTGRES_PASSWORD:="airflow"}"
: "${POSTGRES_DB:="airflow"}"
: "${POSTGRES_EXTRAS:-""}"

AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}${POSTGRES_EXTRAS}"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN

# Default values corresponding to the default compose files
: "${REDIS_PROTO:="redis://"}"
: "${REDIS_HOST:="redis"}"
: "${REDIS_PORT:="6379"}"
: "${REDIS_PASSWORD:=""}"
: "${REDIS_DBNUM:="1"}"

# When Redis is secured by basic auth, it does not handle the username part of basic auth, only a token
if [ -n "$REDIS_PASSWORD" ]; then
  REDIS_PREFIX=":${REDIS_PASSWORD}@"
else
  REDIS_PREFIX=
fi

AIRFLOW__CELERY__BROKER_URL="${REDIS_PROTO}${REDIS_PREFIX}${REDIS_HOST}:${REDIS_PORT}/${REDIS_DBNUM}"
export AIRFLOW__CELERY__BROKER_URL

[ $# -lt 1 ] && usage

# Only wait for backend services in development
[[ -n ${DEVELOPMENT+check} ]] && \
  wait_for "$POSTGRES_HOST" "$POSTGRES_PORT" && \
  wait_for "$REDIS_HOST" "$REDIS_PORT"

case $1 in
  flower)
    exec airflow flower
    ;;
  web)
    airflow upgradedb
    airflow variables -s "sql_path" "/app/sql"

    # TODO: configure things to do in dev environment (if any)
#    [[ -n ${DEVELOPMENT+check} ]] && init_connections && init_variables

    exec airflow webserver -p ${PORT} --workers 4
    ;;
  worker)
    exec airflow worker
    ;;
  scheduler)
    exec airflow scheduler
    ;;
  *)
    exec "$@"
    ;;
esac