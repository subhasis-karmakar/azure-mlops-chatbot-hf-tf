# azure-mlops-chatbot-hf-tf

End-to-end MLOps chatbot using Hugging Face Transformers with TensorFlow, Azure ML SDK v2, MLflow, Terraform, Azure DevOps, and AKS.

## Quick start

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .[dev]
python -m src.training.train --config configs/train_config.yaml
python -m src.evaluation.evaluate --config configs/train_config.yaml --model-dir artifacts/model
uvicorn src.inference.score:app --host 0.0.0.0 --port 8000
```

## Notes

This repo is complete as a production-style starter. Replace Azure-specific values such as subscription, tenant, workspace, service connections, ingress hostnames, and Key Vault secret names before real deployment.
