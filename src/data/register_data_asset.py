from __future__ import annotations
from pathlib import Path
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import Data
from src.utils.azure_ml_utils import get_ml_client

def register_data_asset(*, subscription_id: str, resource_group: str, workspace_name: str, path: str | Path, name: str, version: str, description: str = "") -> Data:
    client = get_ml_client(subscription_id, resource_group, workspace_name)
    asset = Data(path=str(path), type=AssetTypes.URI_FILE, name=name, version=version, description=description)
    return client.data.create_or_update(asset)
