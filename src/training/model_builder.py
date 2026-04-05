from __future__ import annotations
from transformers import TFAutoModelForSequenceClassification

def build_model(model_name: str, num_labels: int):
    return TFAutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)
