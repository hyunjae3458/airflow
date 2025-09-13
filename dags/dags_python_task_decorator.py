from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id = "dags_python_task_operator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 9, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(tast_id="python_tesk_1")
    def print_context(some_input):
        print(some_input)
    
    python_tesk_1 = print_context("task_decorator 실행")