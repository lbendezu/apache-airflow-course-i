import pendulum
import time

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.decorators import task

with DAG(
    dag_id="xcom_basic_test_ds",
    schedule=None,
    catchup=False,
    start_date=pendulum.datetime(2022,1,1,tz="UTC"),
    tags=["xcom_test"]
) as dag:

    t1 = BashOperator(
        task_id="tarea_1",
        bash_command='echo "{{ ti.xcom_push(key="k1", value="computadora") }}" "{{ti.xcom_push(key="k2", value="radio")}}"', dag =dag
    )

    t2 = BashOperator(
        task_id="tarea_2",
        bash_command='echo "{{ ti.xcom_pull(key="k1") }}" "{{ti.xcom_pull(key="k2")}}"', dag =dag
    )

    #t3 = BashOperator(task_id='t3', xcom_push=True, bash_command="ls -la ; $?", dag=dag)
    #t4 = BashOperator(task_id='t4', bash_command='echo "{{ ti.xcom_pull(task_ids="t3") }}"',dag=dag)

    t1 >> t2 # >> t3 >> t4