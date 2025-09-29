from airflow.sdk import DAG
import pendulum
from airflow.providers.standard.sensors.filesystem import FileSensor


with DAG(
    dag_id = "dags_file_sensor",
    schedule="0 7 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    tvCorona19VaccinestatNew_sensor = FileSensor(
        task_id="tvCorona19VaccinestatNew_sensor",
        fs_conn_id="conn_file_opt_airflow_files",
        filepath="tvCorona19VaccinestatNew/{{data_interval_end.in_timezone('Asia/Seoul') | ds_nodash}}/tvCorona19VaccinestatNew.csv",
        recursive=False,
        poke_interval=60,
        timeout=60*60*24, #1일
        mode="reschedule"
    )
