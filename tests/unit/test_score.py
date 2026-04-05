from src.inference.postprocess import apply_fallback, get_fallback_answer

def test_apply_fallback():
    intent, _ = apply_fallback("vpn_reset", 0.2, 0.6)
    assert intent == "unknown"
    assert isinstance(get_fallback_answer(), str)
