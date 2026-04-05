from __future__ import annotations
import pandas as pd

def compute_length_drift(train_df: pd.DataFrame, prod_df: pd.DataFrame) -> float:
    train_mean = train_df["question"].astype(str).str.len().mean()
    prod_mean = prod_df["question"].astype(str).str.len().mean()
    if train_mean == 0:
        return 0.0
    return abs(prod_mean - train_mean) / train_mean

def compute_intent_distribution_drift(train_df: pd.DataFrame, prod_df: pd.DataFrame) -> float:
    train_dist = train_df["intent"].value_counts(normalize=True)
    prod_dist = prod_df["true_intent"].fillna("unknown").value_counts(normalize=True)
    intents = set(train_dist.index).union(set(prod_dist.index))
    drift = 0.0
    for intent in intents:
        drift += abs(train_dist.get(intent, 0.0) - prod_dist.get(intent, 0.0))
    return drift / 2.0

def build_drift_report(train_df: pd.DataFrame, prod_df: pd.DataFrame) -> dict[str, float]:
    return {"question_length_drift": float(compute_length_drift(train_df, prod_df)), "intent_distribution_drift": float(compute_intent_distribution_drift(train_df, prod_df))}
