import pandas as pd

import pythonturtle

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="mi_primer_dag",
    schedule=None,
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    tags=["rapido"]
) as dag:

    @task(task_id="prueba_1")
    def prueba_1(**kwargs):

        df = pd.DataFrame()

        print(type(df))

    prueba_1_load = prueba_1()