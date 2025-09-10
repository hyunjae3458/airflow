from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
import datetime
import pendulum

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", # 분 시 일 월 요일 
    start_date=pendulum.datetime(2025, 9, 1, tz="Asia/Seoul"), # tz는 한국 시간으로
    catchup=False, # False일시 start_date와 오늘날짜 사이의 누락 값을 돌지 않음
) as dag:   
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
