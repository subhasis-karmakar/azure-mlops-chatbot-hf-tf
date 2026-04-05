from __future__ import annotations
import pandas as pd

def summarize_confidence(df: pd.DataFrame) -> dict[str, float]:
    confidence = df["confidence"].astype(float)
    return {"avg_confidence": float(confidence.mean()), "min_confidence": float(confidence.min()), "max_confidence": float(confidence.max())}
