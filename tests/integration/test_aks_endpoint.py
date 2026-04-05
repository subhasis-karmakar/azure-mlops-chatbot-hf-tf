from pathlib import Path

def test_openapi_exists():
    assert Path("deployment/api/openapi.yaml").exists()
