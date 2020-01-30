import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

dag = DAG(
    dag_id="exercise2",
    default_args={"owner": "Schuberg Philis", "start_date": airflow.utils.dates.days_ago(5)},
    schedule_interval=None,
)

print_execution_date = PythonOperator(
    task_id="print_execution_date", python_callable=lambda: print("{{ execution_date }}"), dag=dag
)

wait1 = BashOperator(task_id="wait1", bash_command="sleep 1", dag=dag)
wait5 = BashOperator(task_id="wait1", bash_command="sleep 5", dag=dag)
wait10 = BashOperator(task_id="wait1", bash_command="sleep 10", dag=dag)

theend = DummyOperator(task_id="theend", dag=dag)

print_execution_date >> [wait1, wait5, wait10] >> theend
