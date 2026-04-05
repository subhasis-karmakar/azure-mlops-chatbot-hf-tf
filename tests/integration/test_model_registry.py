from src.registry.promote_model import choose_winner

def test_choose_winner():
    winner = choose_winner({"macro_f1": 0.80}, {"macro_f1": 0.82}, 0.01)
    assert winner == "challenger"
