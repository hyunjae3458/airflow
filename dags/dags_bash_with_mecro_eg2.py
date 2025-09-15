from airflow.sdk import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_with_mecro_eg2",
    schedule="10 0 * * 6#2", # 매월 둘째주 토요일
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    # start_date : 2주전 월요일(배치일 - 19). end_date : 2주전 토요일(배치일 -14)
    bash_task_2 = BashOperator(
        task_id = "bash_task_2",
        env={
            "START_DATE" : "{{ (date_interval_end.timezone('Asia/Seoul') - macros.dateutil.relativedelta(days=19)) | ds}}",
            "END_DATE" : "{{ (date_interval_end.timezone('Asia/Seoul') - macros.dateutil.relativedelta(days=14)) | ds }}"
        },
        bash_command='echo "START_DATE : $START_DATE" && "END_DATE : $END_DATE"'
    )