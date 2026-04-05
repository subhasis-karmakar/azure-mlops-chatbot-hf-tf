from __future__ import annotations

import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def sha1_text(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()

def env_or_default(name: str, default: str = "") -> str:
    return os.getenv(name, default)

def ensure_dir(path: str | Path) -> Path:
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj
