import pandas as pd

import pythonturtle

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="mi_primer_dag",
    schedule="@daily",
    catchup=False,
    start_date=pendulum.datetime(2022, 11, 20, tz="UTC"),
    tags=["rapido"]
) as dag:

    @task(task_id="prueba_1")
    def prueba_1(**kwargs):

        df = pd.DataFrame()

        print(type(df))

    prueba_1_load = prueba_1()






#s3://mi-s3-prueba/

#s3://mi-s3-prueba/sistema_facturacion/2022/01/01/archivo_data.txt
#s3://mi-s3-prueba/sistema_facturacion/2022/01/02/archivo_data.txt
#s3://mi-s3-prueba/sistema_facturacion/2022/01/03/archivo_data.txt
#s3://mi-s3-prueba/sistema_facturacion/2022/01/04/archivo_data.txt
#s3://mi-s3-prueba/sistema_facturacion/2022/01/05/archivo_data.txt