from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

from src.features.label_encoder import load_label_mapping
from src.inference.postprocess import apply_fallback, get_fallback_answer
from src.inference.response_mapper import get_answer_for_intent


class ChatbotPredictor:
    def __init__(
        self,
        model_dir: str | Path,
        faq_path: str | Path,
        confidence_threshold: float = 0.60,
    ) -> None:
        self.model_dir = str(model_dir)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_dir)
        self.model = TFAutoModelForSequenceClassification.from_pretrained(self.model_dir)
        self.label_to_id, self.id_to_label = load_label_mapping(self.model_dir)
        self.faq_df = pd.read_csv(faq_path)
        self.confidence_threshold = confidence_threshold

    def predict(self, question: str) -> dict:
        inputs = self.tokenizer(
            question,
            return_tensors="tf",
            truncation=True,
            padding=True,
        )
        logits = self.model(inputs).logits
        probs = tf.nn.softmax(logits, axis=1).numpy()[0]

        pred_id = int(np.argmax(probs))
        confidence = float(probs[pred_id])
        intent = self.id_to_label[pred_id]

        intent, confidence = apply_fallback(
            intent,
            confidence,
            self.confidence_threshold,
        )

        answer = (
            get_fallback_answer()
            if intent == "unknown"
            else get_answer_for_intent(intent, self.faq_df)
        )

        return {
            "intent": intent,
            "confidence": confidence,
            "answer": answer,
            "model_version": "local",
        }