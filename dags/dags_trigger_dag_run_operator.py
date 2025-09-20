from airflow.sdk import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id ="dags_trigger_dag_run_operator",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    
    start_task = BashOperator(
        task_id="start_task",
        bash_command="echo 'start!'",
    )

    trigger_dag_task = TriggerDagRunOperator(
        task_id="trigger_dag_task",
        trigger_dag_id="dags_python_operator", 
        trigger_run_id=None, 
        execution_date="{{data_interval_start}}", 
        reset_dag_run=True, 
        wait_for_completion=False,
        poke_interval=60,
        allowed_states=["success"],
        failed_states=None
    )

    start_task >> trigger_dag_task