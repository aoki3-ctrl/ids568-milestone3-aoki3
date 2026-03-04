import mlflow

threshold = 0.9

client = mlflow.tracking.MlflowClient()

experiment = mlflow.get_experiment_by_name("milestone3_random_forest")
runs = client.search_runs(experiment.experiment_id)

accuracy = runs[0].data.metrics["accuracy"]

print("Model accuracy:", accuracy)

if accuracy < threshold:
    raise Exception("Model accuracy below threshold")

print("Model passed validation")