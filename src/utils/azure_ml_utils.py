from __future__ import annotations

from pathlib import Path

from azure.ai.ml import MLClient, command
from azure.ai.ml.entities import Environment
from azure.identity import DefaultAzureCredential

from src.utils.io_utils import read_yaml

def get_ml_client(subscription_id: str, resource_group: str, workspace_name: str) -> MLClient:
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    return MLClient(credential, subscription_id, resource_group, workspace_name)

def load_workspace_from_yaml(path: str | Path) -> dict:
    return read_yaml(path)

def build_environment(name: str, image: str, conda_file: str | None = None) -> Environment:
    return Environment(name=name, image=image, conda_file=conda_file)

def build_command_job(*, code: str, command_line: str, environment: str, compute: str, inputs=None, outputs=None):
    return command(code=code, command=command_line, environment=environment, compute=compute, inputs=inputs or {}, outputs=outputs or {})
