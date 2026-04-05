from __future__ import annotations
from pathlib import Path
import pandas as pd

def save_misclassified_examples(df: pd.DataFrame, y_true: list[int], y_pred: list[int], id_to_label: dict[int, str], output_path: str | Path) -> None:
    mis_df = df.copy()
    mis_df["true_label"] = [id_to_label[i] for i in y_true]
    mis_df["predicted_label"] = [id_to_label[i] for i in y_pred]
    mis_df = mis_df[mis_df["true_label"] != mis_df["predicted_label"]]
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    mis_df.to_csv(output_path, index=False)
