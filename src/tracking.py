def log_with_mlflow(params, metrics, model=None, artifact_name="model"):
    """Optional MLflow logging. App works even when MLflow is not installed."""
    try:
        import mlflow
        with mlflow.start_run():
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)
            if model is not None:
                mlflow.sklearn.log_model(model, artifact_name)
        return "MLflow run logged"
    except ImportError:
        return "MLflow not installed; skipped optional tracking"
    except Exception as exc:
        return f"MLflow tracking skipped: {exc}"
