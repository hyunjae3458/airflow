from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task

with DAG(
    dag_id = "dags_python_show_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=True # 9월 1일부터 9월 15일까지 구간 모두 수행
) as dag:
    
    @task(task_id="python_task")
    def show_templates(**kwargs):
        from pprint import pprint # 이쁘게 print해주는 출력문
        pprint(kwargs)

    show_templates()