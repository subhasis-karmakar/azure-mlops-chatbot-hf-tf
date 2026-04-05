from __future__ import annotations
from azure.ai.ml import dsl
from src.utils.azure_ml_utils import get_ml_client

def build_monitor_pipeline(subscription_id: str, resource_group: str, workspace_name: str):
    client = get_ml_client(subscription_id, resource_group, workspace_name)
    @dsl.pipeline(compute="REPLACE_COMPUTE_CLUSTER")
    def monitor_pipeline():
        pass
    return client, monitor_pipeline
