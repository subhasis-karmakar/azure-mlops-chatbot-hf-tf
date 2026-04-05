from __future__ import annotations

def compare_models(champion_metrics: dict, challenger_metrics: dict, min_improvement: float = 0.01) -> bool:
    return float(challenger_metrics["macro_f1"]) >= float(champion_metrics["macro_f1"]) + min_improvement
