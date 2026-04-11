from __future__ import annotations

from azure.ai.ml import MLClient, Output, command
from azure.ai.ml.entities import Environment
from azure.identity import DefaultAzureCredential

SUBSCRIPTION_ID = "6ce8a8a6-d51e-4def-9608-f3aa40eded0c"
RESOURCE_GROUP = "ml-rg"
WORKSPACE_NAME = "my-ml-ws"
COMPUTE_NAME = "my-compute-cluster"


def main() -> None:
    credential = DefaultAzureCredential(
        exclude_interactive_browser_credential=False
    )

    ml_client = MLClient(
        credential=credential,
        subscription_id=SUBSCRIPTION_ID,
        resource_group_name=RESOURCE_GROUP,
        workspace_name=WORKSPACE_NAME,
    )

    env = Environment(
        name="hf-tf-chatbot-env",
        description="HF TensorFlow chatbot training environment",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
        conda_file="environment/conda.yml",
    )

    job = command(
        code=".",
        command=(
            "python -m src.training.train "
            "--config configs/train_config.yaml "
            "--output-dir ${{outputs.model_output}}"
        ),
        environment=env,
        compute=COMPUTE_NAME,
        experiment_name="azure-mlops-chatbot",
        display_name="chatbot-train-job",
        outputs={
            "model_output": Output(type="uri_folder"),
        },
    )

    returned_job = ml_client.jobs.create_or_update(job)
    print("Submitted job:", returned_job.name)
    print("Studio URL:", returned_job.studio_url)


if __name__ == "__main__":
    main()