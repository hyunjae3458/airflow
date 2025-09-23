from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from hooks.custom_postgres_hook import CustomPostgresHook

with DAG(
    dag_id = "dags_python_with_custom_hook_bulk_load",
    schedule="0 7 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    def insrt_postgres(postgres_conn_id, tbi_nm, file_nm, **kwargs):
        custom_postgres_hook = CustomPostgresHook(postgres_conn_id=postgres_conn_id)
        # 가져온 csv파일에서 ,를 바꾸고 헤더를 없애고 수정이면 replace 추가면 append를 나타내게 함
        custom_postgres_hook.bulk_load(table_name=tbi_nm, file_name=file_nm, delimiter=",", is_header=True, is_replace="True")

    insert_postgres = PythonOperator(
        task_id="insert_postgres",
        python_callable=insrt_postgres,
        op_kwargs={"postgres_conn_id" : "conn_db_postgres_custom",
                   "tbi_nm" : "TbCorona19CountStatus_bulk2",
                   "file_nm" : "/opt/airflow/files/TbCorona19CountStatus/{{data_interval_end.in_timezone('Asia/Seoul') | ds_nodash}}/filesTbCorona19CountStatus.csv"}
    )

    insert_postgres