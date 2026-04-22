from __future__ import annotations

from dataclasses import dataclass

from modules.account_manager.manager import Account, AccountManager
from modules.proxy_manager.manager import ProxyEndpoint, ProxyManager


@dataclass(slots=True)
class RouteSelection:
    account: Account
    proxy: ProxyEndpoint | None


class ApiRouter:
    def __init__(self, account_manager: AccountManager, proxy_manager: ProxyManager | None = None) -> None:
        self.account_manager = account_manager
        self.proxy_manager = proxy_manager

    def select_route(
        self,
        model: str | None,
        excluded_accounts: set[str] | None = None,
        excluded_proxies: set[str] | None = None,
    ) -> RouteSelection:
        account = self.account_manager.next_account(model, excluded_accounts)
        proxy = None
        if self.proxy_manager is not None:
            proxy = self.proxy_manager.next_proxy(model, excluded_proxies)
        return RouteSelection(account=account, proxy=proxy)

