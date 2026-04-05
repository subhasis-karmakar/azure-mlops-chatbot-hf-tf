from __future__ import annotations

from pathlib import Path
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_faq_data(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    logger.info("Loaded FAQ data with %s rows from %s", len(df), path)
    return df

def load_chat_logs(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    logger.info("Loaded chat logs with %s rows from %s", len(df), path)
    return df
