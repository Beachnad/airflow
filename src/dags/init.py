
from __future__ import print_function
import airflow
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow import models
from airflow.settings import Session
import logging
import os


args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(7),
    'provide_context': True
}


def init():
    logging.info('Creating connections, pool and sql path')

    session = Session()

    def create_new_conn(session, attributes):
        new_conn = models.Connection()
        new_conn.conn_id = attributes.get("conn_id")
        new_conn.conn_type = attributes.get('conn_type')
        new_conn.host = attributes.get('host')
        new_conn.port = attributes.get('port')
        new_conn.schema = attributes.get('schema')
        new_conn.login = attributes.get('login')
        new_conn.set_password(attributes.get('password'))

        session.add(new_conn)
        session.commit()

    # TODO: Create a non-root user for airflow to use.
    create_new_conn(session,
                    {"conn_id": "dwh",
                     "conn_type": "postgres",
                     "host": os.getenv('POSTGRES_HOST'),
                     "port": os.getenv('POSTGRES_PORT'),
                     "schema": "postgres",
                     "login": 'worker',
                     "password": os.getenv('WORKER_PASS')})

    new_pool = models.Pool()
    new_pool.pool = "sportsref"
    new_pool.slots = 1
    new_pool.description = "Allows max. 1 connections to sportsreference.com."
    session.add(new_pool)
    session.commit()

    session.close()


dag = airflow.DAG(
    'init',
    schedule_interval="@once",
    is_paused_upon_creation=False,
    default_args=args,
    max_active_runs=1)

t1 = PythonOperator(task_id='init',
                    python_callable=init,
                    provide_context=False,
                    dag=dag)