from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from src.evaluation.confusion_matrix import plot_confusion_matrix
from src.evaluation.error_analysis import save_misclassified_examples
from src.evaluation.metrics import build_classification_report, compute_classification_metrics
from src.features.label_encoder import load_label_mapping
from src.utils.io_utils import read_yaml, write_json

def predict_labels(model_dir: str | Path, questions: list[str], max_length: int = 128) -> list[int]:
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = TFAutoModelForSequenceClassification.from_pretrained(model_dir)
    encodings = tokenizer(questions, padding=True, truncation=True, max_length=max_length, return_tensors="tf")
    logits = model(encodings).logits.numpy()
    return np.argmax(logits, axis=1).tolist()

def evaluate_from_model_dir(model_dir: str | Path, test_path: str | Path, config: dict) -> dict[str, float]:
    test_df = pd.read_csv(test_path)
    label_to_id, id_to_label = load_label_mapping(model_dir)
    y_true = test_df["intent"].map(label_to_id).astype(int).tolist()
    y_pred = predict_labels(model_dir, test_df["question"].tolist(), max_length=int(config["max_length"]))
    metrics = compute_classification_metrics(y_true, y_pred)
    artifacts_dir = Path(config["artifacts_dir"])
    labels = [id_to_label[i] for i in range(len(id_to_label))]
    report = build_classification_report(y_true, y_pred, labels)
    write_json(report, artifacts_dir / "classification_report.json")
    plot_confusion_matrix(y_true, y_pred, labels, artifacts_dir / "confusion_matrix.png")
    save_misclassified_examples(test_df, y_true, y_pred, id_to_label, artifacts_dir / "misclassified_examples.csv")
    return metrics

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--model-dir", required=True)
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = read_yaml(args.config)
    metrics = evaluate_from_model_dir(args.model_dir, config["test_path"], config)
    write_json(metrics, Path(config["artifacts_dir"]) / "metrics.json")
    print(metrics)

if __name__ == "__main__":
    main()
