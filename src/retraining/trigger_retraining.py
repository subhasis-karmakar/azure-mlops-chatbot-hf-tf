from __future__ import annotations

def should_trigger_retraining(*, drift_report: dict[str, float], new_labeled_samples: int, min_new_samples: int, data_drift_threshold: float) -> bool:
    return new_labeled_samples >= min_new_samples or drift_report.get("question_length_drift", 0.0) > data_drift_threshold or drift_report.get("intent_distribution_drift", 0.0) > data_drift_threshold
