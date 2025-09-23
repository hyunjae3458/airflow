from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.operators.python import PythonOperator

with DAG(
    dag_id = "dags_python_with_postgres_hook",
    schedule=None,
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    
    def insrt_postgres(postgres_conn_id,**kwargs):
        from airflow.providers.postgres.hooks.postgres import PostgresHook
        from contextlib import closing

        postgres_hook = PostgresHook(postgres_conn_id)
        with closing(postgres_hook.get_conn()) as conn:
            with closing(conn.cursor()) as cursor:
                dag_id = kwargs.get("ti").dag_id
                task_id = kwargs.get("ti").task_id
                run_id = kwargs.get("ti").run_id
                msg = "hook insrt 수행"
                sql = "insert into py_opr_drct_insrt values (%s,%s,%s,%s);"
                cursor.execute(sql,(dag_id,task_id,run_id,msg))
                conn.commit()

    insert_postgres_with_hook = PythonOperator(
        task_id = "insert_postgres_with_hook",
        python_callable=insrt_postgres,
        op_kwargs={"postgres_conn_id" : "conn_db_postgres_custom"}
    )

    
    insert_postgres_with_hook