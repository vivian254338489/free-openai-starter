from pathlib import Path

from fastapi.testclient import TestClient

from core.server import build_app, load_yaml


def test_load_yaml_reads_example_accounts_file() -> None:
    config = load_yaml(Path("config/accounts.example.yaml"))

    assert "accounts" in config
    assert len(config["accounts"]) >= 2


def test_app_exposes_health_check() -> None:
    app = build_app(
        accounts_path="config/accounts.example.yaml",
        proxies_path="config/proxies.example.yaml",
        routing_path="config/routing.example.yaml",
    )

    client = TestClient(app)
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
