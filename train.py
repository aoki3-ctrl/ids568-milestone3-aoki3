import mlflow
import mlflow.sklearn
import argparse
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--n_estimators", type=int, default=100)
parser.add_argument("--max_depth", type=int, default=5)
args = parser.parse_args()

# Load processed data
df = pd.read_csv("processed_data.csv")

X = df.drop("target", axis=1)
y = df["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Set experiment
mlflow.set_experiment("milestone3_random_forest")

with mlflow.start_run():

    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)

    # Log parameters
    mlflow.log_param("n_estimators", args.n_estimators)
    mlflow.log_param("max_depth", args.max_depth)

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Log model artifact
    mlflow.sklearn.log_model(model, "model")

    print(f"Accuracy: {accuracy}")