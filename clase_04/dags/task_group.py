import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.decorators import task_group

with DAG(
    dag_id='contenedor_task_group',
    start_date=pendulum.datetime(2022,1,1,tz="UTC"),
    schedule="@daily",
    catchup=False,
    default_args={'retries':1}
):
    @task_group()
    def grupo_1():
        tarea_1 = EmptyOperator(task_id="tarea_1")
        tarea_2 = EmptyOperator(task_id="tarea_2")

    tarea_3 = EmptyOperator(task_id="tarea_3")

    grupo_1() >> tarea_3