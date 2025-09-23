from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

with DAG(
    dag_id = "dags_python_with_postgres_hook_bulk_load",
    schedule="0 7 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    def insrt_postgres(postgres_conn_id,tbi_nm,file_nm,**kwagrs):
        postgres_hook = PostgresHook(postgres_conn_id)
        postgres_hook.bulk_load(tbi_nm,file_nm)

    insert_postgres = PythonOperator(
        task_id="insert_postgres",
        python_callable=insrt_postgres,
        op_kwargs={"postgres_conn_id" : "conn_db_postgres_custom",
                   "tbi_nm" : "TbCorona19CountStatus_bulk1",
                   "file_nm" : "/opt/airflow/files/TbCorona19CountStatus/{{data_interval_end.in_timezone('Asia/Seoul') | ds_nodash}}/TbCorona19CountStatus.csv"}
    )