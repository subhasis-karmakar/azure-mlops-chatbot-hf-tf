from __future__ import annotations
import re
import pandas as pd

WHITESPACE_RE = re.compile(r"\s+")
PUNCT_RE = re.compile(r"[^\w\s]")

def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = PUNCT_RE.sub(" ", text)
    text = WHITESPACE_RE.sub(" ", text)
    return text.strip()

def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    copy_df = df.copy()
    copy_df["question"] = copy_df["question"].astype(str).apply(clean_text)
    copy_df["answer"] = copy_df["answer"].astype(str).str.strip()
    copy_df["intent"] = copy_df["intent"].astype(str).str.strip()
    return copy_df
