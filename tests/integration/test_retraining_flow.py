from src.retraining.champion_challenger import compare_models

def test_compare_models():
    assert compare_models({"macro_f1": 0.8}, {"macro_f1": 0.82}, 0.01)
