from __future__ import annotations
import json
from src.utils.helpers import sha1_text, utc_now_iso
from src.utils.logger import get_logger

logger = get_logger(__name__)

def log_prediction_event(question: str, prediction: dict, latency_ms: float) -> None:
    payload = {
        "timestamp": utc_now_iso(),
        "question_hash": sha1_text(question),
        "predicted_intent": prediction.get("intent"),
        "confidence": prediction.get("confidence"),
        "answer_preview": str(prediction.get("answer", ""))[:80],
        "latency_ms": round(float(latency_ms), 2),
        "model_version": prediction.get("model_version", "unknown"),
        "fallback": prediction.get("intent") == "unknown",
    }
    logger.info(json.dumps(payload))
