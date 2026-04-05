from __future__ import annotations
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support

def compute_classification_metrics(y_true, y_pred) -> dict[str, float]:
    accuracy = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average="macro")
    weighted_precision, weighted_recall, weighted_f1, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted")
    return {"accuracy": float(accuracy), "macro_precision": float(precision), "macro_recall": float(recall), "macro_f1": float(f1), "weighted_precision": float(weighted_precision), "weighted_recall": float(weighted_recall), "weighted_f1": float(weighted_f1)}

def build_classification_report(y_true, y_pred, target_names: list[str]) -> dict:
    return classification_report(y_true, y_pred, target_names=target_names, output_dict=True)
