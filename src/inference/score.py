from __future__ import annotations
import os
import time
from pathlib import Path
from fastapi import FastAPI, HTTPException
from src.inference.predict import ChatbotPredictor
from src.inference.request_schema import PredictRequest, PredictResponse
from src.monitoring.collect_logs import log_prediction_event
from src.utils.io_utils import read_yaml

CONFIG_PATH = os.getenv("CHATBOT_CONFIG_PATH", "configs/train_config.yaml")
config = read_yaml(CONFIG_PATH)
MODEL_DIR = Path(os.getenv("CHATBOT_MODEL_DIR", config.get("output_dir", "artifacts/model")))
FAQ_PATH = Path(os.getenv("CHATBOT_FAQ_PATH", config.get("faq_path", "data/raw/faq_data.csv")))
CONFIDENCE_THRESHOLD = float(config.get("thresholds", {}).get("fallback_confidence", 0.60))
app = FastAPI(title="Chatbot Inference API", version="1.0.0")
_predictor: ChatbotPredictor | None = None

def get_predictor() -> ChatbotPredictor:
    global _predictor
    if _predictor is None:
        if not MODEL_DIR.exists():
            raise RuntimeError(f"Model directory does not exist: {MODEL_DIR}")
        _predictor = ChatbotPredictor(MODEL_DIR, FAQ_PATH, CONFIDENCE_THRESHOLD)
    return _predictor

@app.get("/health")
def health() -> dict:
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    try:
        start = time.perf_counter()
        result = get_predictor().predict(request.question)
        latency_ms = (time.perf_counter() - start) * 1000
        log_prediction_event(request.question, result, latency_ms)
        return PredictResponse(**result)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
