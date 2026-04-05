from __future__ import annotations
import argparse
from azure.ai.ml.entities import Model
from src.utils.azure_ml_utils import get_ml_client
from src.utils.io_utils import read_json, read_yaml

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-config", required=True)
    parser.add_argument("--model-dir", required=True)
    parser.add_argument("--metrics-path", required=True)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--version", default="1")
    parser.add_argument("--dataset-version", default="1")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    ws = read_yaml(args.workspace_config)
    metrics = read_json(args.metrics_path)
    min_macro_f1 = ws.get("thresholds", {}).get("min_macro_f1", 0.7)
    if float(metrics["macro_f1"]) < min_macro_f1:
        raise SystemExit(f"Model not registered: macro_f1 {metrics['macro_f1']} < {min_macro_f1}")
    client = get_ml_client(ws["subscription_id"], ws["resource_group"], ws["workspace_name"])
    model = Model(path=args.model_dir, name=args.model_name, version=args.version, description="Chatbot intent classification model", tags={"dataset_version": args.dataset_version, "macro_f1": str(metrics["macro_f1"])})
    client.models.create_or_update(model)
    print(f"Registered model {args.model_name}:{args.version}")

if __name__ == "__main__":
    main()
