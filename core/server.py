from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from core.app import create_app
from core.providers.openai_compatible import OpenAICompatibleProxyClient
from modules.account_manager.manager import Account, AccountManager
from modules.proxy_manager.manager import ProxyEndpoint, ProxyManager
from modules.rate_limit_handler.retry import RateLimitHandler, RetryPolicy


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def build_client(
    accounts_path: str | Path,
    proxies_path: str | Path | None = None,
    routing_path: str | Path | None = None,
) -> OpenAICompatibleProxyClient:
    accounts_config = load_yaml(accounts_path)
    account_manager = AccountManager(
        Account(
            name=item["name"],
            api_key=item["api_key"],
            base_url=item["base_url"],
            models=item.get("models"),
        )
        for item in accounts_config.get("accounts", [])
    )

    proxy_manager = None
    if proxies_path:
        proxies_config = load_yaml(proxies_path)
        proxy_items = proxies_config.get("proxies", [])
        if proxy_items:
            proxy_manager = ProxyManager(
                ProxyEndpoint(name=item["name"], url=item["url"], models=item.get("models"))
                for item in proxy_items
            )

    policy = RetryPolicy()
    if routing_path:
        routing_config = load_yaml(routing_path)
        retry = routing_config.get("retry_policy", {})
        policy = RetryPolicy(
            max_attempts=retry.get("max_attempts", 3),
            base_backoff_seconds=retry.get("base_backoff_seconds", 0.5),
            cooldown_seconds=retry.get("cooldown_seconds", 15.0),
        )

    return OpenAICompatibleProxyClient(
        account_manager=account_manager,
        proxy_manager=proxy_manager,
        rate_limit_handler=RateLimitHandler(policy),
    )


def build_app(
    accounts_path: str | Path = "config/accounts.example.yaml",
    proxies_path: str | Path | None = "config/proxies.example.yaml",
    routing_path: str | Path | None = "config/routing.example.yaml",
):
    return create_app(build_client(accounts_path, proxies_path, routing_path))

