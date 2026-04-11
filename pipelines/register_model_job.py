from __future__ import annotations

from pathlib import Path

from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model
from azure.identity import DefaultAzureCredential

SUBSCRIPTION_ID = "6ce8a8a6-d51e-4def-9608-f3aa40eded0c"
RESOURCE_GROUP = "ml-rg"
WORKSPACE_NAME = "my-ml-ws"

JOB_NAME = "hungry_cumin_rqx3x8r95r"
MODEL_NAME = "hf-tf-chatbot-model"
DOWNLOAD_DIR = Path("downloaded_job_output")


def main() -> None:
    ml_client = MLClient(
        DefaultAzureCredential(exclude_interactive_browser_credential=False),
        SUBSCRIPTION_ID,
        RESOURCE_GROUP,
        WORKSPACE_NAME,
    )

    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading model_output from job:", JOB_NAME)
    ml_client.jobs.download(
        name=JOB_NAME,
        download_path=str(DOWNLOAD_DIR),
        output_name="model_output",
    )

    candidates = [
        DOWNLOAD_DIR / "named-outputs" / "model_output",
        DOWNLOAD_DIR / "model_output",
        DOWNLOAD_DIR,
    ]

    model_dir = None
    for candidate in candidates:
        if candidate.exists():
            files = list(candidate.rglob("config.json"))
            if files:
                model_dir = files[0].parent
                break

    if model_dir is None:
        raise FileNotFoundError(
            f"Could not find a model folder under {DOWNLOAD_DIR.resolve()}"
        )

    print("Using local model directory:", model_dir)

    model = Model(
        path=str(model_dir),
        name=MODEL_NAME,
        type="custom_model",
        description="HF TensorFlow chatbot model",
        tags={
            "framework": "tensorflow",
            "task": "intent-classification",
            "job_name": JOB_NAME,
        },
    )

    registered = ml_client.models.create_or_update(model)
    print("Registered model:", registered.name)
    print("Version:", registered.version)


if __name__ == "__main__":
    main()