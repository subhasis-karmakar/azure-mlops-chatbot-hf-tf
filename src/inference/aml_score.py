from __future__ import annotations

import json
import logging
import os 
import sys
from pathlib import Path

from src.inference.predict import ChatbotPredictor

logger = logging.getLogger(__name__)

predictor: ChatbotPredictor | None = None


def init() -> None:
    global predictor

    model_root = Path(os.getenv("AZUREML_MODEL_DIR", ".")) / "model_output"
    faq_path = Path(os.getenv("CHATBOT_FAQ_PATH", "data/raw/faq_data.csv"))

    logger.info("AZUREML_MODEL_DIR=%s", model_root)
    logger.info("FAQ path=%s", faq_path)
    model_version = os.getenv("MODEL_VERSION", "unknown")
    predictor = ChatbotPredictor(
        model_dir=model_root,
        faq_path=faq_path,
        confidence_threshold=0.4,
    )
    predictor.model_version = model_version

    logger.info("Model initialized successfully")


def run(raw_data: str) -> dict:
    try:
        if predictor is None:
            raise RuntimeError("Predictor is not initialized")

        payload = json.loads(raw_data)

        if isinstance(payload, dict) and "question" in payload:
            question = payload["question"]
        else:
            raise ValueError("Input payload must contain 'question'")

        return predictor.predict(question)

    except Exception as exc:
        logger.exception("Scoring failed")
        return {"error": str(exc)}