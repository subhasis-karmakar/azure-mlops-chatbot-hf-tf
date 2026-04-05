from __future__ import annotations
import platform
from src.utils.helpers import utc_now_iso

def build_model_metadata(model_name: str, metrics: dict, dataset_version: str, git_sha: str = "unknown") -> dict:
    return {"model_name": model_name, "dataset_version": dataset_version, "git_sha": git_sha, "training_timestamp": utc_now_iso(), "framework": "tensorflow-transformers", "python_version": platform.python_version(), "metrics": metrics}
