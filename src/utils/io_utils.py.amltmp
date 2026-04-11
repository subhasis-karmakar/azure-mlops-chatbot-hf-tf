from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def read_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)

def write_json(data: Any, path: str | Path) -> None:
    ensure_parent(path)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)

def read_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)
