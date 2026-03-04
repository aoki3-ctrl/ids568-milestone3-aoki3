# MLflow Experiment Tracking

## Experiment Runs Comparison

The screenshot below shows the MLflow experiment tracking interface comparing five Random Forest runs with different hyperparameters. Each run logs the parameters (`n_estimators`, `max_depth`) and the resulting model accuracy.

![MLflow Experiment Runs](screenshots/experiment_runs.png)

Five runs were executed using different hyperparameter configurations for the Random Forest classifier. MLflow tracked the parameters and evaluation metrics for each run, allowing easy comparison of model performance. The experiment shows that the configuration with `n_estimators = 100` and `max_depth = 5` achieved the highest accuracy of 1.0 on the validation set.