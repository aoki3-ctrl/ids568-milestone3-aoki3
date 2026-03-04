# MLOps Pipeline – Milestone 3

This project implements an end-to-end MLOps pipeline using MLflow, Airflow, and GitHub Actions to automate model training, validation, and registration.

# Pipeline Architecture

The pipeline follows a modular architecture consisting of three main stages:

1. Data Preprocessing
2. Model Training
3. Model Registration

The workflow is orchestrated using **Apache Airflow**, while **MLflow** is used for experiment tracking and model registry management. The pipeline ensures that every stage of the machine learning lifecycle is reproducible and traceable. The Airflow DAG orchestrates the machine learning pipeline by executing preprocessing, model training, and model registration tasks sequentially. Each step produces reproducible artifacts that are tracked using MLflow, ensuring traceability across the entire model lifecycle.


The main pipeline tasks are:

```
preprocess_data → train_model → register_model
```

Each stage is executed sequentially and managed by the Airflow DAG.


# Airflow Execution

Apache Airflow orchestrates the pipeline through a Directed Acyclic Graph(DAG). The DAG automates the execution of preprocessing, model training, and model registration tasks.

The three tasks in the DAG include:

• Preprocess_data: prepares and cleans the dataset before training
• Train_model: trains the Random Forest classifier and logs metrics to MLflow
• Register_model: registers the best-performing model into the MLflow Model Registry

Airflow ensures task dependencies are respected and provides monitoring through the Airflow UI.

### DAG Idempotency and Lineage Guarantees

The Airflow DAG is designed to be idempotent, meaning that repeated executions produce consistent and reproducible outputs without unintended side effects. Each task in the pipeline performs deterministic operations using version-controlled code and tracked datasets.

Lineage tracking is supported through MLflow experiment logging. Each training run records parameters, metrics, and artifacts, enabling full traceability of how a model was produced. This guarantees that the origin of any registered model can be traced back to its training run and associated configuration.




# CI-Based Model Governance Approach

Continuous Integration is implemented using **GitHub Actions**. Each push to the repository triggers a workflow that automatically:

1. Installs dependencies
2. Runs preprocessing
3. Trains the model
4. Validates model performance

The validation step uses a **model accuracy threshold** to ensure only models meeting the required performance level pass the pipeline.

This helps enforce quality control before models move further in the deployment lifecycle.This helps maintain model reliability and ensures consistent model quality.


# MLflow Experiment Tracking

MLflow is used to track machine learning experiments. Each training run logs:

* Hyperparameters
* Evaluation metrics
* Trained model artifacts

These runs are stored in the MLflow tracking server and can be compared through the MLflow UI. The best-performing model from the experiments is registered in the **MLflow Model Registry**, enabling version control and lifecycle management of models.
MLflow ensures full traceability of experiments and allows reproducibility of training runs.


### Setup and Execution Instructions

To reproduce the pipeline locally, follow these steps:

1. Clone the repository:

```
git clone <repository-url>
cd repository-name
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run preprocessing and training manually:

```
python preprocess.py
python train.py
```

4. Start the MLflow UI:

```
mlflow ui
```

5. Launch Airflow to execute the pipeline DAG and monitor execution through the Airflow web interface.


## Operational Notes

### Retry Strategies and Failure Handling

The Airflow DAG includes built-in retry mechanisms to handle temporary task failures. Each task is configured with retry parameters such as the number of retry attempts and delay intervals. If a task fails, Airflow automatically retries execution before marking the task as failed.

### Monitoring and Alerting

Pipeline health can be monitored through the Airflow web interface and MLflow tracking dashboard. Monitoring model performance metrics and training runs helps identify anomalies or degradation in model quality. Alerting systems can be integrated to notify operators when failures occur or performance thresholds are violated.

### Rollback Procedures

If a newly trained model performs poorly in production, rollback procedures allow reverting to a previously registered model version in the MLflow Model Registry. Maintaining version history ensures that stable models can be restored quickly without interrupting service availability.
