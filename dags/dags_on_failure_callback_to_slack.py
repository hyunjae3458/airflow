from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import timedelta
import pendulum
from config.on_failure_callback_to_slack import on_failure_callback_to_slack

with DAG(
    dag_id ="dags_on_failure_callback_to_slack",
    schedule="*/20 * * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False,
    default_args={
        "on_failure_callback" : on_failure_callback_to_slack,
        "execution_timeout" : timedelta(seconds=60)
    } 
) as dag:
    task_slp_90 = BashOperator(
        task_id = "task_slp_90",
        bash_command="sleep 90"
    )

    task_ext_1 = BashOperator(
        trigger_rule="all_done",
        task_id="task_ext_1",
        bash_command="exit 1"
    )

    task_slp_90 >> task_ext_1