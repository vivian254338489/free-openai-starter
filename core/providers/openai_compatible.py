from __future__ import annotations

import asyncio
from typing import Any

import httpx

from modules.account_manager.manager import AccountManager
from modules.api_router.router import ApiRouter
from modules.proxy_manager.manager import ProxyManager
from modules.rate_limit_handler.retry import RateLimitHandler


class OpenAICompatibleProxyClient:
    def __init__(
        self,
        account_manager: AccountManager,
        rate_limit_handler: RateLimitHandler,
        proxy_manager: ProxyManager | None = None,
        timeout_seconds: float = 60.0,
    ) -> None:
        self.account_manager = account_manager
        self.proxy_manager = proxy_manager
        self.router = ApiRouter(account_manager, proxy_manager)
        self.rate_limit_handler = rate_limit_handler
        self.timeout_seconds = timeout_seconds

    async def forward(self, path: str, body: dict[str, Any]) -> tuple[int, dict[str, Any]]:
        model = body.get("model")
        excluded_accounts: set[str] = set()
        excluded_proxies: set[str] = set()

        for attempt in range(1, self.rate_limit_handler.policy.max_attempts + 1):
            route = self.router.select_route(model, excluded_accounts, excluded_proxies)
            headers = {
                "Authorization": f"Bearer {route.account.api_key}",
                "Content-Type": "application/json",
            }
            try:
                async with httpx.AsyncClient(
                    base_url=route.account.base_url.rstrip("/"),
                    timeout=self.timeout_seconds,
                    proxy=route.proxy.url if route.proxy else None,
                ) as client:
                    response = await client.post(f"/{path.lstrip('/')}", json=body, headers=headers)
            except httpx.HTTPError:
                self.account_manager.mark_failure(route.account.name, self.rate_limit_handler.policy.cooldown_seconds)
                excluded_accounts.add(route.account.name)
                if route.proxy:
                    self.proxy_manager.mark_failure(route.proxy.name, self.rate_limit_handler.policy.cooldown_seconds)
                    excluded_proxies.add(route.proxy.name)
                if attempt >= self.rate_limit_handler.policy.max_attempts:
                    raise
                await asyncio.sleep(self.rate_limit_handler.policy.base_backoff_seconds)
                continue

            if response.status_code < 400:
                self.account_manager.mark_success(route.account.name)
                if route.proxy:
                    self.proxy_manager.mark_success(route.proxy.name)
                return response.status_code, response.json()

            decision = self.rate_limit_handler.decision(response.status_code, attempt)
            if not decision.should_retry:
                payload = self._safe_json(response)
                return response.status_code, payload

            if decision.switch_account:
                self.account_manager.mark_failure(route.account.name, decision.cooldown_seconds)
                excluded_accounts.add(route.account.name)
            if route.proxy and decision.cooldown_seconds > 0:
                self.proxy_manager.mark_failure(route.proxy.name, decision.cooldown_seconds)
                excluded_proxies.add(route.proxy.name)
            await asyncio.sleep(decision.sleep_seconds)

        return 502, {"error": {"message": "upstream retry budget exhausted"}}

    @staticmethod
    def _safe_json(response: httpx.Response) -> dict[str, Any]:
        try:
            return response.json()
        except ValueError:
            return {"error": {"message": response.text}}

