from airflow.sdk import DAG
from airflow.providers.smtp.operators.smtp import EmailOperator
import datetime
import pendulum

with DAG(
    dag_id="dags_email.operator",
    schedule="0 8 1 * *", # 매월 1일 아침 8시
    start_date=pendulum.datetime(2025, 9, 1, tz="Asia/Seoul"), # tz는 한국 시간으로
    catchup=False
) as dag:
    send_email_task = EmailOperator(
        task_id = "send_email_task",
        conn_id="conn_smtp_gmail",
        to="fredsonata@naver.com",
        # cc= 는 참조할 사람
        subject="Airflow 성공메일",
        html_content="Airflow 작업이 완료되었습니다"
    )