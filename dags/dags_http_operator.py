from airflow.sdk import DAG,task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.http.operators.http import HttpOperator
import pendulum
import datetime

with DAG(
    dag_id ="dags_http_operator",
    schedule=None,
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    tpss_route_section_time = HttpOperator(
        task_id="tpss_route_section_time",
        http_conn_id="openapi.seoul.go.kr",
        endpoint="{{var.value.apikey_openapi_seoul_go_kr}}/jsoin/tpssRouteSectionTime/1/10/",
        method="GET",
        headers={"Content-Type" : "application/json",
                 "Charset": "utf-8",
                 "Accept" : "*/*"}
    )

    @task(task_id="python_2")
    def python_2(**kwargs):
        ti = kwargs["ti"]
        result = ti.xcom_pull(task_ids="tpss_route_section_time")
        import json
        from pprint import pprint

        pprint(json.loads(result))

    tpss_route_section_time >> python_2()
