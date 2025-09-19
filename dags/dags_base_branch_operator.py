from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.branch import BaseBranchOperator
import pendulum

with DAG(
    dag_id ="dags_base_branch_opertator",
    schedule="10 9 * * *",
    start_date=pendulum.datetime(2025, 9 , 1, tz="Asia/Seoul"),
    catchup=False 
) as dag:
    class CustomBranchOperator(BaseBranchOperator):
        def choose_branch(self,context):  # context 객체 안에 파라미터들이 다 들어있음 ex)data_intervel_start   
            import random 
            print(context)
            item_lst = ["A","B","C"]
            selected_item = random.choice(item_lst)
            if selected_item == "A":
                return "task_a"
            elif selected_item in ["B","C"]:
                return ["task_b","task_c"]
        
    custom_branch_operator = CustomBranchOperator(task_id="python_branch_task")

    def common_func(**kwargs):
        return kwargs["selected"]

    task_a=PythonOperator(
        task_id="task_a",
        python_callable=common_func,
        op_kwargs={"selected" : "A"}
    )

    task_b=PythonOperator(
        task_id="task_b",
        python_callable=common_func,
        op_kwargs={"selected" : "B"}
    )

    task_c=PythonOperator(
        task_id="task_c",
        python_callable=common_func,
        op_kwargs={"selected" : "C"}
    )

    custom_branch_operator >> [task_a,task_b,task_c]