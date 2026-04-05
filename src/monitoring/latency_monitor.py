from __future__ import annotations
import pandas as pd

def summarize_latency(df: pd.DataFrame) -> dict[str, float]:
    latencies = df["latency_ms"].astype(float)
    return {"p50_latency_ms": float(latencies.quantile(0.50)), "p95_latency_ms": float(latencies.quantile(0.95)), "max_latency_ms": float(latencies.max())}
