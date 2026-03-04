# MLflow Experiment Tracking
## Experiment Overview
Multiple Random Forest models were trained with different hyperparameters using MLflow experiment tracking. Each run logs parameters, metrics, and model artifacts to allow comparison and reproducibility.

## Experiment Runs Comparison

The screenshot below shows the MLflow experiment tracking interface comparing five Random Forest runs with different hyperparameters. Each run logs the parameters (`n_estimators`, `max_depth`) and the resulting model accuracy.

![MLflow Experiment Runs](screenshots/experiment_runs.png)

Five runs were executed using different hyperparameter configurations for the Random Forest classifier. MLflow tracked the parameters and evaluation metrics for each run, allowing easy comparison of model performance. The experiment shows that the configuration with `n_estimators = 100` and `max_depth = 5` achieved the highest accuracy of 1.0 on the validation set.


## Risks and Monitoring
Potential risks include overfitting due to limited dataset size and sensitivity to hyperparameter changes. In production, monitoring should track model accuracy, latency, and data drift to ensure continued performance.