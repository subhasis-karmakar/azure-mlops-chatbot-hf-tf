from __future__ import annotations
from pathlib import Path
from typing import Any
import mlflow

def configure_tracking(tracking_uri: str | None, experiment_name: str) -> None:
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)

def log_params(params: dict[str, Any]) -> None:
    mlflow.log_params(params)

def log_metrics(metrics: dict[str, float]) -> None:
    mlflow.log_metrics(metrics)

def log_artifacts(path: str | Path) -> None:
    mlflow.log_artifacts(str(path))
