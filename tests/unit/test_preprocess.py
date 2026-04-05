from src.data.preprocess import clean_text

def test_clean_text():
    assert clean_text("  Hello, WORLD! ") == "hello world"
