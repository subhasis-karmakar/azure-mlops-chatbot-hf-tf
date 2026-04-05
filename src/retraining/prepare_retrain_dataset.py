from __future__ import annotations
import pandas as pd

def prepare_retrain_dataset(history_df: pd.DataFrame, new_labeled_df: pd.DataFrame) -> pd.DataFrame:
    merged = pd.concat([history_df, new_labeled_df], ignore_index=True)
    return merged.drop_duplicates(subset=["question", "intent"]).reset_index(drop=True)
