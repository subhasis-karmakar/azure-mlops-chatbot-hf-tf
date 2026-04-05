from src.evaluation.metrics import compute_classification_metrics

def test_compute_metrics():
    metrics = compute_classification_metrics([0, 1, 1], [0, 1, 0])
    assert "macro_f1" in metrics
    assert 0 <= metrics["accuracy"] <= 1
