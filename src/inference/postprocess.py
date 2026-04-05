from __future__ import annotations

def apply_fallback(intent: str, confidence: float, threshold: float) -> tuple[str, float]:
    if confidence < threshold:
        return "unknown", confidence
    return intent, confidence

def get_fallback_answer() -> str:
    return "I am not fully sure. Please rephrase your question or contact support."
