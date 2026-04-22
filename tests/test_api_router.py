from modules.account_manager.manager import Account, AccountManager
from modules.api_router.router import ApiRouter
from modules.proxy_manager.manager import ProxyEndpoint, ProxyManager


def test_api_router_selects_matching_account_and_proxy() -> None:
    accounts = AccountManager(
        [
            Account(name="kimi-primary", api_key="key-a", base_url="https://api.example.com", models=["kimi"]),
            Account(name="general-fallback", api_key="key-b", base_url="https://api.example.com"),
        ],
        time_fn=lambda: 0.0,
    )
    proxies = ProxyManager(
        [
            ProxyEndpoint(name="cn-exit", url="http://cn:8080", models=["kimi"]),
            ProxyEndpoint(name="global-exit", url="http://global:8080"),
        ],
        time_fn=lambda: 0.0,
    )

    route = ApiRouter(accounts, proxies).select_route("kimi")

    assert route.account.name == "kimi-primary"
    assert route.proxy.name == "cn-exit"


def test_api_router_can_route_without_proxy() -> None:
    accounts = AccountManager(
        [Account(name="only", api_key="key-a", base_url="https://api.example.com")],
        time_fn=lambda: 0.0,
    )

    route = ApiRouter(accounts, None).select_route("minimax")

    assert route.account.name == "only"
    assert route.proxy is None
