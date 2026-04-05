from __future__ import annotations
from typing import Iterable
import pandas as pd

REQUIRED_COLUMNS = ["question", "answer", "intent", "source", "last_updated"]

def validate_required_columns(df: pd.DataFrame, required_columns: Iterable[str] = REQUIRED_COLUMNS) -> None:
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def validate_non_empty(df: pd.DataFrame) -> None:
    for col in ["question", "answer", "intent"]:
        if df[col].isna().any() or (df[col].astype(str).str.strip() == "").any():
            raise ValueError(f"Column '{col}' contains null or empty values.")

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=["question", "intent"]).reset_index(drop=True)

def validate_faq_schema(df: pd.DataFrame) -> pd.DataFrame:
    validate_required_columns(df)
    validate_non_empty(df)
    clean_df = remove_duplicates(df)
    if clean_df["intent"].nunique() < 2:
        raise ValueError("At least two intents are required for classification.")
    return clean_df
