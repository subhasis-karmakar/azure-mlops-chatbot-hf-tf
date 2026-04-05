from __future__ import annotations
from pathlib import Path
from typing import Iterable
from src.utils.io_utils import read_json, write_json

def fit_label_encoder(labels: Iterable[str]) -> tuple[dict[str, int], dict[int, str]]:
    unique_labels = sorted(set(labels))
    label_to_id = {label: idx for idx, label in enumerate(unique_labels)}
    id_to_label = {idx: label for label, idx in label_to_id.items()}
    return label_to_id, id_to_label

def save_label_mapping(label_to_id: dict[str, int], output_dir: str | Path) -> None:
    output_dir = Path(output_dir)
    write_json(label_to_id, output_dir / "label_to_id.json")
    write_json({str(v): k for k, v in label_to_id.items()}, output_dir / "id_to_label.json")

def load_label_mapping(model_dir: str | Path) -> tuple[dict[str, int], dict[int, str]]:
    label_to_id = read_json(Path(model_dir) / "label_to_id.json")
    raw_id_to_label = read_json(Path(model_dir) / "id_to_label.json")
    id_to_label = {int(k): v for k, v in raw_id_to_label.items()}
    return label_to_id, id_to_label
