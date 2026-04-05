PYTHON ?= python

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .[dev]

format:
	black src tests
	isort src tests

lint:
	flake8 src tests
	mypy src --ignore-missing-imports

test:
	pytest -q

train-local:
	$(PYTHON) -m src.training.train --config configs/train_config.yaml

eval-local:
	$(PYTHON) -m src.evaluation.evaluate --config configs/train_config.yaml --model-dir artifacts/model

run-api:
	uvicorn src.inference.score:app --host 0.0.0.0 --port 8000
