FROM circleci/python:3.7.5

COPY . .
COPY requirements.txt .
ENV PYTHONPATH "${PYTHONPATH}:/airflow/dags/"
RUN sudo pip install -r requirements.txt