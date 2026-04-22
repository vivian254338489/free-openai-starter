from modules.proxy_manager.manager import ProxyEndpoint, ProxyManager


def test_proxy_manager_rotates_available_proxies() -> None:
    manager = ProxyManager(
        [
            ProxyEndpoint(name="proxy-a", url="http://proxy-a:8080"),
            ProxyEndpoint(name="proxy-b", url="http://proxy-b:8080"),
        ],
        time_fn=lambda: 0.0,
    )

    assert manager.next_proxy().name == "proxy-a"
    assert manager.next_proxy().name == "proxy-b"
    assert manager.next_proxy().name == "proxy-a"


def test_proxy_manager_skips_unhealthy_proxy_until_cooldown_expires() -> None:
    clock = {"now": 0.0}
    manager = ProxyManager(
        [
            ProxyEndpoint(name="proxy-a", url="http://proxy-a:8080"),
            ProxyEndpoint(name="proxy-b", url="http://proxy-b:8080"),
        ],
        time_fn=lambda: clock["now"],
    )

    assert manager.next_proxy().name == "proxy-a"
    manager.mark_failure("proxy-a", cooldown_seconds=20.0)
    assert manager.next_proxy().name == "proxy-b"

    clock["now"] = 21.0
    assert manager.next_proxy().name == "proxy-a"

