import datetime
import time

import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.latest_only import LatestOnlyOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.decorators import task

with DAG(
    dag_id='trigger_rules_test_datascience2',
    schedule=datetime.timedelta(hours=4),
    start_date=pendulum.datetime(2021,1,1,tz="UTC"),
    catchup=False,
    tags=['trigger_test']
) as dag:

    @task(task_id="task_1")
    def tarea_1(**kwargs):
        print("tarea_1")
        time.sleep(10)

    @task(task_id="task_2", trigger_rule=TriggerRule.NONE_FAILED)
    def tarea_2(**kwargs):
        print("tarea_2")
        #time.sleep(10)
        raise ValueError("Error")

    @task(task_id="task_3")
    def tarea_3(**kwargs):
        print("tarea_3")
        #time.sleep(10)
        raise ValueError("Error")

    @task(task_id="task_4", trigger_rule=TriggerRule.ALWAYS)
    def tarea_4(**kwargs):
        print("tarea_4")
        time.sleep(10)

    tarea_1_var = tarea_1()
    tarea_2_var = tarea_2()
    tarea_3_var = tarea_3()
    tarea_4_var = tarea_4()

    tarea_1_var >> [tarea_2_var, tarea_3_var] >> tarea_4_var