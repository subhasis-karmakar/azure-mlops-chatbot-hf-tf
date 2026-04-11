from __future__ import annotations

from azure.ai.ml import MLClient
from azure.ai.ml.entities import Model
from azure.identity import DefaultAzureCredential

SUBSCRIPTION_ID = "6ce8a8a6-d51e-4def-9608-f3aa40eded0c"
RESOURCE_GROUP = "ml-rg"
WORKSPACE_NAME = "my-ml-ws"

JOB_NAME = "calm_rainbow_6qwz60lkhj"
MODEL_NAME = "hf-tf-chatbot-model"
OUTPUT_NAME = "model_output"


def main() -> None:
    ml_client = MLClient(
        DefaultAzureCredential(exclude_interactive_browser_credential=False),
        SUBSCRIPTION_ID,
        RESOURCE_GROUP,
        WORKSPACE_NAME,
    )

    job = ml_client.jobs.get(JOB_NAME)

    if OUTPUT_NAME not in job.outputs:
        raise KeyError(
            f"Job {JOB_NAME} does not contain an output named '{OUTPUT_NAME}'"
        )

    # Build the Azure ML job output URI explicitly.
    model_output_uri = f"azureml://jobs/{JOB_NAME}/outputs/{OUTPUT_NAME}/paths/"

    print("Registering model directly from:", model_output_uri)

    model = Model(
        path=model_output_uri,
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