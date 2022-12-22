from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(dag_id="get_info_adidas",
    start_date=datetime(2021,1,1),
    schedule_interval="@daily",
    catchup=False) as dag:

    @task
    def extract(my_param):
        return my_param

    @task
    def transform(my_param):
        return my_param

    @task
    def load(my_param):
        return my_param

    load(transform(extract(100)))