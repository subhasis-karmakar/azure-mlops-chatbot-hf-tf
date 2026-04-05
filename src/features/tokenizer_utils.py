from __future__ import annotations
from typing import Iterable
from transformers import AutoTokenizer

def get_tokenizer(model_name: str):
    return AutoTokenizer.from_pretrained(model_name)

def tokenize_texts(texts: Iterable[str], tokenizer, max_length: int = 128):
    return tokenizer(list(texts), padding=True, truncation=True, max_length=max_length, return_tensors="tf")
