import pendulum
import time

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="max_runs",
    schedule="@yearly",
    catchup=True,
    start_date=pendulum.datetime(2015, 1, 1, tz="UTC"),
    max_active_runs=3,
    tags=["rapido"]
) as dag:

    @task(task_id="paso_1")
    def paso_1(**kwargs):
        print("a dormir 1")
        time.sleep(10)
        print("desperté 1")


    @task(task_id="paso_2")
    def paso_2(**kwargs):
        print("a dormir 2")
        time.sleep(10)
        print("desperté 2")

    @task(task_id="paso_3")
    def paso_3(**kwargs):
        print("a dormir 3")
        time.sleep(10)
        print("desperté 3")

    paso_1_task = paso_1()
    paso_2_task = paso_2()
    paso_3_task = paso_3()

    paso_1_task >> paso_2_task >> paso_3_task