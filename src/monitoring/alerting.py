from __future__ import annotations

def evaluate_alerts(*, data_drift_report: dict[str, float], model_drift_report: dict[str, float], latency_report: dict[str, float], data_drift_threshold: float, fallback_rate_threshold: float, latency_p95_threshold: float) -> dict:
    alerts = []
    if data_drift_report.get("question_length_drift", 0.0) > data_drift_threshold:
        alerts.append("question_length_drift")
    if data_drift_report.get("intent_distribution_drift", 0.0) > data_drift_threshold:
        alerts.append("intent_distribution_drift")
    if model_drift_report.get("fallback_rate", 0.0) > fallback_rate_threshold:
        alerts.append("fallback_rate")
    if latency_report.get("p95_latency_ms", 0.0) > latency_p95_threshold:
        alerts.append("latency_p95")
    return {"status": "alert" if alerts else "ok", "alerts": alerts}
