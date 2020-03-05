FROM python:3.7.5-slim
# Based off of https://github.com/mozilla/telemetry-airflow/blob/master/Dockerfile.dev

# add a non-privileged user for installing and running the application
RUN mkdir /app && \
    chown 10001:10001 /app /usr/local/ && \
    groupadd --gid 10001 app && \
    useradd --no-create-home --uid 10001 --gid 10001 --home-dir /app app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-transport-https build-essential curl git libpq-dev python-dev \
        default-libmysqlclient-dev gettext sqlite3 libffi-dev libsasl2-dev \
        lsb-release gnupg vim && \
    apt-get remove -y lsb-release gnupg && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Python dependencies
COPY requirements.txt /tmp/
# Switch to /tmp to install dependencies outside home dir
WORKDIR /tmp

RUN pip install --upgrade pip
RUN export SLUGIFY_USES_TEXT_UNIDECODE=yes && pip install --no-cache-dir -r requirements.txt

# Switch back to home directory
WORKDIR /app

COPY ./src/airflow.cfg airflow.cfg
COPY ./src/entrypoint.sh entrypoint.sh

USER 10001

ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DEPLOY_ENVIRONMENT=dev \
    DEVELOPMENT=1 \
    DEPLOY_TAG=master

ENV AIRFLOW_HOME=/app \
    AIRFLOW_AUTHENTICATE=False \
    AIRFLOW_AUTH_BACKEND=airflow.contrib.auth.backends.password_auth \
    AIRFLOW_DATABASE_URL=postgres://postgres:password@postgres:5432/master \
    AIRFLOW__CORE__FERNET_KEY="pXRP7RNfYVB3uOU6w1A9wlgnRdS7pYSKLqeAuyfgChY=" \
    AIRFLOW_SECRET_KEY="pXRP7RNfYVB3uOU6w1A9wlgnRdS7pYSKLqeAuyfgChY=" \
    AIRFLOW__SCHEDULER__CATCHUP_BY_DEFAULT=True \
    URL="http://localhost:8000" \
    WEBSERVER_USE_RBAC="False" \
    AIRFLOW__CORE__LOAD_EXAMPLES=False

EXPOSE $PORT

# Using /bin/bash as the entrypoint works around some volume mount issues on Windows
# where volume-mounted files do not have execute bits set.
# https://github.com/docker/compose/issues/2301#issuecomment-154450785 has additional background.
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

CMD ["web"]
