from airflow.sdk import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = "dags_bash_with_template",
    schedule="10 6 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_t1 = BashOperator(
        task_id = "bash_t1",
        bash_command='echo "data_interval_end: {{ data_interval_end }}"'
    )

    bash_t2 = BashOperator(
        task_id = "bash_t2",
        env={
            "START_DATE": "{{ data_interval_start | ds }}", # yyyy 10자리 형식
            "END_DATE" : "{{ data_interval_end | ds }}"
        },
        bash_command="echo $START_DATE && $END_DATE"
    )

    bash_t1 >> bash_t2