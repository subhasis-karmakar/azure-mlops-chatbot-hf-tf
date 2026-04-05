import pandas as pd
from src.monitoring.data_drift import build_drift_report

def test_build_drift_report():
    train = pd.DataFrame({"question": ["a", "bb"], "intent": ["x", "y"]})
    prod = pd.DataFrame({"question": ["aaa"], "true_intent": ["x"]})
    report = build_drift_report(train, prod)
    assert "question_length_drift" in report
