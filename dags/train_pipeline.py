from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess


# Task 1: Preprocess data
def preprocess_data():
    subprocess.run(["python", "/Users/afokeoki/ids568-milestone3-aoki3/preprocess.py"], check=True)


# Task 2: Train model
def train_model():
    subprocess.run(["python", "/Users/afokeoki/ids568-milestone3-aoki3/train.py"], check=True)


# Task 3: Register model to MLflow
def register_model():

    import mlflow
    from mlflow.tracking import MlflowClient

    mlflow.set_tracking_uri("sqlite:///mlflow.db")

    client = MlflowClient()

    experiment = mlflow.get_experiment_by_name("milestone3_random_forest")

    runs = client.search_runs(experiment.experiment_id)

    if runs:
        run_id = runs[0].info.run_id
        model_uri = f"runs:/{run_id}/model"

        mlflow.register_model(
            model_uri=model_uri,
            name="rf_model"
        )

        print("Model registered successfully")


# Failure callback
def on_failure_callback(context):
    print("Task failed:", context)


default_args = {
    "owner": "mlops",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
    "on_failure_callback": on_failure_callback
}


with DAG(
    dag_id="train_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args
) as dag:

    preprocess = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_data
    )

    train = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )

    register = PythonOperator(
        task_id="register_model",
        python_callable=register_model
    )

    # Task order
    preprocess >> train >> register