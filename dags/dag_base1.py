from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(dag_id="test1",
    start_date=datetime(2021,1,1),
    schedule_interval="@daily",
    catchup=False) as dag:

    @task
    def tarea1(test):
        return test

    @task
    def tarea2(test):
        return test

    @task
    def tarea3(test):
        return test

    tarea1(tarea2(tarea3(10)))