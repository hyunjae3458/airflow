from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
import datetime
import pendulum
from airflow.models import Variable

with DAG(
    dag_id="dags_bash_with_variable",
    schedule="10 9 * * *",
    start_date=pendulum.datetime(2025, 9, 1, tz="Asia/Seoul"), # tz는 한국 시간으로
    catchup=False
) as dag:
    var_value = Variable.get("sample_key")

    bash_ver_1 = BashOperator(
        task_id="bash_ver_1",
        bash_command=f"echo variable: {var_value}"
    )

    bash_ver_2 = BashOperator( # 권고 방식
        task_id="bash_ver_2",
        bash_command="echo variable:{{ var.value.sample_key}}"
    )

    bash_ver_1 >> bash_ver_2