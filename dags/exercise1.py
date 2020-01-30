from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

dag = DAG(dag_id="exercise1", default_args={"owner": "Schuberg Philis"}, schedule_interval=None)

task1 = DummyOperator(task_id="task1")
task2 = DummyOperator(task_id="task2")
task3 = DummyOperator(task_id="task3")
task4 = DummyOperator(task_id="task4")
task5 = DummyOperator(task_id="task5")

task1 >> task2 >> [task3, task4] >> task5
