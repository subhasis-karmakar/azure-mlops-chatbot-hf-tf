from __future__ import annotations
from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    question: str = Field(..., min_length=3)

class PredictResponse(BaseModel):
    intent: str
    confidence: float
    answer: str
    model_version: str
