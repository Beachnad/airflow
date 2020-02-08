from datetime import datetime, timedelta, date

from airflow import DAG
import airflow

from common.operators.data_gen import PandasToPostgresOperator
from scripts.sports import get_adv_boxscores


default_args = {
    'owner': 'Airflow',
    'depends_on_past': False,  # Jan 2nd must wait for Jan 1st
    'start_date': airflow.utils.dates.days_ago(7),
    'email': ['src@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('sportsref_ncaab', default_args=default_args, schedule_interval='0 0 * 11-12,1-3 *')

t1 = PandasToPostgresOperator(
    destination_conn_id='dwh',
    destination_table='staging.box_scores',
    preoperator="""    
DELETE FROM staging.box_scores
WHERE "date" <  '{{ ds }}'
AND   "date" >= '{{ prev_ds }}'
""",
    fun=get_adv_boxscores,
    fun_args=('{{ prev_ds }}', '{{ ds }}'),
    pool='sportsref',
    task_id='stage_boxscores',
    dag=dag
)
