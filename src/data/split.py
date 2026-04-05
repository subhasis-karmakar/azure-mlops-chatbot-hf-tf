from __future__ import annotations
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils.helpers import ensure_dir

def split_dataset(df: pd.DataFrame, train_ratio: float = 0.7, val_ratio: float = 0.15, test_ratio: float = 0.15, seed: int = 42) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if round(train_ratio + val_ratio + test_ratio, 6) != 1.0:
        raise ValueError("train_ratio + val_ratio + test_ratio must sum to 1.0")
    train_df, temp_df = train_test_split(df, test_size=1 - train_ratio, stratify=df["intent"], random_state=seed)
    relative_test = test_ratio / (val_ratio + test_ratio)
    val_df, test_df = train_test_split(temp_df, test_size=relative_test, stratify=temp_df["intent"], random_state=seed)
    return train_df.reset_index(drop=True), val_df.reset_index(drop=True), test_df.reset_index(drop=True)

def save_splits(output_dir: str | Path, train_df: pd.DataFrame, val_df: pd.DataFrame, test_df: pd.DataFrame) -> None:
    output_path = ensure_dir(output_dir)
    train_df.to_csv(output_path / "train.csv", index=False)
    val_df.to_csv(output_path / "val.csv", index=False)
    test_df.to_csv(output_path / "test.csv", index=False)
