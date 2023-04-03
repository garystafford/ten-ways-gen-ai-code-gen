#  write a DAG that prints all environment variables to the logs
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

DAG_ID = os.path.basename(__file__).replace(".py", "")

DEFAULT_ARGS = {
    "owner": "garystafford",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
}


def print_env_vars():
    for key, value in os.environ.items():
        print(f"{key}={value}")

    return "Done!"


with DAG(
    
