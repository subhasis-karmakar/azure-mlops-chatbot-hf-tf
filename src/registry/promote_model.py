from __future__ import annotations

def choose_winner(champion_metrics: dict, challenger_metrics: dict, min_improvement: float = 0.01) -> str:
    champion = float(champion_metrics.get("macro_f1", 0.0))
    challenger = float(challenger_metrics.get("macro_f1", 0.0))
    return "challenger" if challenger >= champion + min_improvement else "champion"
