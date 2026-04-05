from __future__ import annotations
from pathlib import Path
import tensorflow as tf

def get_callbacks(output_dir: str | Path) -> list[tf.keras.callbacks.Callback]:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    return [
        tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=2, restore_best_weights=True),
        tf.keras.callbacks.ModelCheckpoint(filepath=str(Path(output_dir) / "best.weights.h5"), monitor="val_loss", save_best_only=True, save_weights_only=True),
    ]
