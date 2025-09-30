from airflow import Dataset
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
import pendulum

dataset_dags_dataset_producer_1 = Dataset("dags_dataset_producer_1")

with DAG(
    dag_id = "dags_dataset_producer_1",
    schedule="10 1 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    bash_task = BashOperator(
        task_id="bash_task",
        outlets=[dataset_dags_dataset_producer_1],
        bash_command="echo 'producer_1 수행 완료'"
    )