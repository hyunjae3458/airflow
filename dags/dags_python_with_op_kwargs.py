from airflow.sdk import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id = "dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id = "regist2_t1",
        python_callable=regist,
        op_args=["hjkim","man","kr","seoul"],
        op_kwargs={"email":"fredsonata@naver.com","phone": "010"}
    )

    regist2_t1