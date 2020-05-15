import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False,
            "email_on_failure": False,
            "email_on_retry": False,
            "email": "matt@aaaio.solutions",
            "retries": 1,
            "retry_delay": timedelta(minutes=5)
        }

with DAG(dag_id="state_table_write_dim", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    states_dim_defensive = BashOperator(
            task_id="states_dim_defensive",
            bash_command="python /Users/mlivingston/Documents/covid-app/airflow_home/dags/scripts/"
                         "states_dim_defensive.py"
    )

    states_dim = BashOperator(
            task_id="states_dim",
            bash_command="python /Users/mlivingston/Documents/covid-app/airflow_home/dags/scripts/"
                         "states_dim.py"
    )

    states_dim_defensive >> states_dim

