from __future__ import annotations
import pandas as pd

def get_answer_for_intent(intent: str, faq_df: pd.DataFrame) -> str:
    match = faq_df[faq_df["intent"] == intent]
    if match.empty:
        return "I am not sure. Please rephrase your question or contact support."
    return str(match.iloc[0]["answer"])
