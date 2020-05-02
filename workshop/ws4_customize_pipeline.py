from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'User',
    'depends_on_past': False,
    'start_date': datetime(2015, 12, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@daily',
}


dag = DAG('workshop4_custom', catchup=False, default_args=default_args)


t1 = PythonOperator(
    task_id='hello_world',
    python_callable=print,
    op_args=['Hello World!'],
    dag=dag,
)

t2 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t3 = BashOperator(
    task_id='list_gcs',
    bash_command='gsutil ls gs://us-central1-airflow-62239854-bucket/',
    dag=dag,
)

t1 >> [t2,t3]