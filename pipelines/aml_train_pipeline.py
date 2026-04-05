from __future__ import annotations
from azure.ai.ml import Input, dsl
from src.utils.azure_ml_utils import get_ml_client

def build_pipeline(subscription_id: str, resource_group: str, workspace_name: str):
    client = get_ml_client(subscription_id, resource_group, workspace_name)
    @dsl.pipeline(compute="REPLACE_COMPUTE_CLUSTER")
    def training_pipeline(raw_faq: Input):
        pass
    return client, training_pipeline
