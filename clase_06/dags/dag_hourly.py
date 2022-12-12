import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(    
    schedule="@hourly",
    dag_id="dag_hourly",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    tags=["rapido"]
) as dag:

    @task(task_id="prueba_2")
    def prueba_2(**kwargs):
        print("test")

    prueba_2_load = prueba_2()