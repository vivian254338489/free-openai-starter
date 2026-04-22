from __future__ import annotations

from dataclasses import dataclass, field
from time import monotonic
from typing import Callable, Iterable


@dataclass(slots=True)
class ProxyEndpoint:
    name: str
    url: str
    models: list[str] | None = None
    metadata: dict[str, str] = field(default_factory=dict)
    cooldown_until: float = 0.0
    consecutive_failures: int = 0

    def supports_model(self, model: str | None) -> bool:
        return not model or not self.models or model in self.models

    def is_available(self, now: float) -> bool:
        return now >= self.cooldown_until


class ProxyManager:
    def __init__(
        self,
        proxies: Iterable[ProxyEndpoint],
        time_fn: Callable[[], float] | None = None,
    ) -> None:
        self._proxies = list(proxies)
        self._time_fn = time_fn or monotonic
        self._cursor = 0
        if not self._proxies:
            raise ValueError("at least one proxy is required")

    @property
    def proxies(self) -> list[ProxyEndpoint]:
        return self._proxies

    def next_proxy(self, model: str | None = None, excluded_names: set[str] | None = None) -> ProxyEndpoint:
        excluded_names = excluded_names or set()
        now = self._time_fn()
        for offset in range(len(self._proxies)):
            index = (self._cursor + offset) % len(self._proxies)
            proxy = self._proxies[index]
            if proxy.name in excluded_names:
                continue
            if not proxy.supports_model(model):
                continue
            if not proxy.is_available(now):
                continue
            self._cursor = (index + 1) % len(self._proxies)
            return proxy
        raise RuntimeError(f"no available proxy for model={model!r}")

    def mark_failure(self, proxy_name: str, cooldown_seconds: float) -> None:
        proxy = self._find(proxy_name)
        proxy.consecutive_failures += 1
        proxy.cooldown_until = self._time_fn() + cooldown_seconds

    def mark_success(self, proxy_name: str) -> None:
        proxy = self._find(proxy_name)
        proxy.consecutive_failures = 0
        proxy.cooldown_until = 0.0

    def _find(self, proxy_name: str) -> ProxyEndpoint:
        for proxy in self._proxies:
            if proxy.name == proxy_name:
                return proxy
        raise KeyError(f"unknown proxy: {proxy_name}")

