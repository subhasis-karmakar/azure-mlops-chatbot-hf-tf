from src.features.label_encoder import fit_label_encoder
from src.training.model_builder import build_model

def test_fit_label_encoder():
    label_to_id, id_to_label = fit_label_encoder(["b", "a", "a"])
    assert label_to_id["a"] == 0
    assert id_to_label[1] == "b"

def test_model_builder_symbol_exists():
    assert callable(build_model)
