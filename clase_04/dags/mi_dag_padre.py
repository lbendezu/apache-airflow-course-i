import datetime
import pendulum

from airflow import DAG
#from airflow.dags.mi_subdag import mi_primer_subdag
from airflow.operators.empty import EmptyOperator
from airflow.operators.subdag import SubDagOperator

def mi_primer_subdag(parent_dag, child_dag, args):

    dag_subdag = DAG(
        dag_id=f'{parent_dag}.{child_dag}',
        default_args=args,
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
        catchup=False,
        schedule="@daily"
    )

    for i in range(10):
        EmptyOperator(
            task_id=f'{child_dag}-tarea-{i+1}',
            default_args=args,
            dag=dag_subdag
        )

    return dag_subdag

DAG_NAME = "mi_dag_padre"

with DAG(
    dag_id=DAG_NAME,
    default_args={"retries": 2},
    start_date=datetime.datetime(2022,1,1),
    schedule="@once",
    tags=['subdag']
) as dag:
    primera_tarea = EmptyOperator(
        task_id='primera_tarea'
    )

    mi_sub_dag_1 = SubDagOperator(
        task_id='mi_sub_dag_1',
        subdag=mi_primer_subdag(DAG_NAME, 'mi_sub_dag_1', dag.default_args)
    )

    tercera_tarea = EmptyOperator(
        task_id='tercera_tarea'
    )

    mi_sub_dag_2 = SubDagOperator(
        task_id='mi_sub_dag_2',
        subdag=mi_primer_subdag(DAG_NAME, 'mi_sub_dag_2', dag.default_args)
    )

    tarea_final = EmptyOperator(
        task_id='tarea_final'
    )

    primera_tarea >> mi_sub_dag_1 >> tercera_tarea >> mi_sub_dag_2 >> tarea_final