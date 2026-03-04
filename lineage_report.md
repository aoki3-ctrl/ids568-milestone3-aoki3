# MLflow Experiment Tracking
## Experiment Overview
Multiple Random Forest models were trained with different hyperparameters using MLflow experiment tracking. Each run logs parameters, metrics, and model artifacts to allow comparison and reproducibility.

## Experiment Runs Comparison

The screenshot below shows the MLflow experiment tracking interface comparing five Random Forest runs with different hyperparameters. Each run logs the parameters (`n_estimators`, `max_depth`) and the resulting model accuracy.

![MLflow Experiment Runs](Screenshots/experiment_runs.png)

Five runs were executed using different hyperparameter configurations for the Random Forest classifier. MLflow tracked the parameters and evaluation metrics for each run, allowing easy comparison of model performance. The experiment shows that the configuration with `n_estimators = 100` and `max_depth = 5` achieved the highest accuracy of 1.0 on the validation set.

Run 3 produced the highest validation accuracy, indicating better generalization performance compared to the other runs. Increasing the `max_depth` allowed the model to capture more complex relationships in the dataset without causing significant overfitting.

Additionally:

* The model maintained stable performance during evaluation.
* The accuracy metric exceeded the threshold used in the validation script.
* MLflow tracked this run with the best metric values among all experiments.

For these reasons, Run 3 was selected as the best-performing model and registered in the MLflow Model Registry as `rf_model`.

## Risks and Monitoring
Potential risks include overfitting due to limited dataset size and sensitivity to hyperparameter changes. In production, monitoring should track model accuracy, latency, and data drift to ensure continued performance. Although Run 3 achieved the best performance among the evaluated models, several operational risks should be considered before deploying the model to production;
First, the model was trained on a relatively small dataset (the Iris dataset), which may not represent real-world variability. If the model were applied to a larger or more diverse dataset, its performance could degrade due to unseen patterns or data drift.

Second, hyperparameter tuning was limited to a small set of configurations. There is a possibility that other parameter combinations could yield improved performance or more stable predictions.
To mitigate these risks, the following monitoring practices are recommended:

• Performance monitoring: Track prediction accuracy over time to detect model degradation.
• Data drift detection: Monitor feature distributions to identify changes in incoming data.
• Retraining triggers: Schedule periodic retraining when model performance drops below a defined threshold.

Implementing monitoring and alerting mechanisms will ensure that the production model maintains reliable performance over time.



