from __future__ import annotations
import pandas as pd

def summarize_model_drift(scored_df: pd.DataFrame) -> dict[str, float]:
    confidence = scored_df["confidence"].astype(float)
    fallback = scored_df["intent"].astype(str).eq("unknown")
    return {"avg_confidence": float(confidence.mean()), "low_confidence_rate": float((confidence < 0.60).mean()), "fallback_rate": float(fallback.mean())}
