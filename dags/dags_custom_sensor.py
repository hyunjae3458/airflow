from airflow.sdk import DAG
import pendulum
from sensors.seoul_api_data_sensor import SeoulApiDataSensor

with DAG(
    dag_id = "dags_custom_sensor",
    schedule="0 7 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    tb_corona_19_count_status_sensor = SeoulApiDataSensor(
        task_id="tb_corona_19_count_status_sensor",
        dataset_nm = "TbCorona19CountStatus",
        base_dt_col="S_DT",
        day_off=0,
        poke_interval=600, # 10분
        mode="reschedule"
    )

    tv_corona_19_vaccine_stat_new_sensor = SeoulApiDataSensor(
        task_id="tv_corona_19_vaccine_stat_new_sensor",
        dataset_nm = "tvCorona19VaccinestatNew",
        base_dt_col="S_VC_DT",
        day_off=-1,
        poke_interval=600, # 10분
        mode="reschedule"
    )