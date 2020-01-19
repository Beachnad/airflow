from airflow.dag import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.

from sportsreference.ncaab.boxscore import Boxscores

from common.operators.data_gen import PandasToPostgresOperator

