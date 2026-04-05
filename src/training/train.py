from __future__ import annotations
import argparse
import random
from pathlib import Path
import mlflow
import numpy as np
import tensorflow as tf
from src.data.ingest import load_faq_data
from src.data.preprocess import preprocess_dataframe
from src.data.split import save_splits, split_dataset
from src.data.validate import validate_faq_schema
from src.evaluation.evaluate import evaluate_from_model_dir
from src.training.mlflow_logger import configure_tracking, log_artifacts, log_metrics, log_params
from src.training.trainer import train_model
from src.utils.helpers import ensure_dir
from src.utils.io_utils import read_yaml, write_json
from src.utils.logger import get_logger

logger = get_logger(__name__)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--skip-split", action="store_true")
    return parser.parse_args()

def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

def main() -> None:
    args = parse_args()
    config = read_yaml(args.config)
    ensure_dir(config["artifacts_dir"])
    set_seed(int(config["random_seed"]))
    if not args.skip_split:
        faq_df = load_faq_data(config["faq_path"])
        faq_df = validate_faq_schema(faq_df)
        faq_df = preprocess_dataframe(faq_df)
        train_df, val_df, test_df = split_dataset(faq_df, seed=int(config["random_seed"]))
        Path(config["train_path"]).parent.mkdir(parents=True, exist_ok=True)
        save_splits(Path(config["train_path"]).parent, train_df, val_df, test_df)
    else:
        train_df = load_faq_data(config["train_path"])
        val_df = load_faq_data(config["val_path"])
    mlflow_cfg = config.get("mlflow", {})
    configure_tracking(mlflow_cfg.get("tracking_uri"), mlflow_cfg.get("experiment_name", "default"))
    with mlflow.start_run():
        log_params({"model_name": config["model_name"], "max_length": config["max_length"], "batch_size": config["batch_size"], "epochs": config["epochs"], "learning_rate": config["learning_rate"]})
        train_model(train_df, val_df, config)
        metrics = evaluate_from_model_dir(config["output_dir"], config["test_path"], config)
        write_json(metrics, Path(config["artifacts_dir"]) / "metrics.json")
        log_metrics(metrics)
        log_artifacts(config["artifacts_dir"])
        logger.info("Training complete. Metrics: %s", metrics)

if __name__ == "__main__":
    main()
