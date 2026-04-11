from __future__ import annotations

from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    CodeConfiguration,
    Environment,
    ManagedOnlineDeployment,
    ManagedOnlineEndpoint,
)
from azure.identity import DefaultAzureCredential

SUBSCRIPTION_ID = "6ce8a8a6-d51e-4def-9608-f3aa40eded0c"
RESOURCE_GROUP = "ml-rg"
WORKSPACE_NAME = "my-ml-ws"

ENDPOINT_NAME = "cbot-subhasis-03"
DEPLOYMENT_NAME = "blue"
MODEL_NAME = "hf-tf-chatbot-model"
MODEL_VERSION = "9"


def main() -> None:
    ml_client = MLClient(
        DefaultAzureCredential(exclude_interactive_browser_credential=False),
        SUBSCRIPTION_ID,
        RESOURCE_GROUP,
        WORKSPACE_NAME,
    )

    endpoint = ManagedOnlineEndpoint(
        name=ENDPOINT_NAME,
        description="Chatbot managed online endpoint",
        auth_mode="key",
    )

    ml_client.begin_create_or_update(endpoint).result()
    print(f"Endpoint created: {ENDPOINT_NAME}")

    env = Environment(
        name="hf-tf-chatbot-infer-env",
        description="Inference environment for HF TensorFlow chatbot",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
        conda_file="environment/conda.yml",
    )

    deployment = ManagedOnlineDeployment(
        name=DEPLOYMENT_NAME,
        endpoint_name=ENDPOINT_NAME,
        model=f"{MODEL_NAME}:{MODEL_VERSION}",
        environment=env,
        code_configuration=CodeConfiguration(
            code=".",
            scoring_script="src/inference/aml_score.py",
        ),
        environment_variables={
            "PYTHONPATH": "/var/azureml-app/azure-mlops-chatbot-hf-tf",
            "CHATBOT_FAQ_PATH": "/var/azureml-app/azure-mlops-chatbot-hf-tf/data/raw/faq_data.csv",
            "MODEL_VERSION": MODEL_VERSION,
        },
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )

    print(f"Check: endpoint {ENDPOINT_NAME} exists")
    ml_client.begin_create_or_update(deployment).result()
    print(f"Deployment created: {DEPLOYMENT_NAME}")

    endpoint = ml_client.online_endpoints.get(ENDPOINT_NAME)
    endpoint.traffic = {DEPLOYMENT_NAME: 100}
    ml_client.begin_create_or_update(endpoint).result()

    print("Deployment live")


if __name__ == "__main__":
    main()