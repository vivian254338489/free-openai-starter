from __future__ import annotations

from dataclasses import dataclass, field
from time import monotonic
from typing import Callable, Iterable


@dataclass(slots=True)
class Account:
    name: str
    api_key: str
    base_url: str
    models: list[str] | None = None
    metadata: dict[str, str] = field(default_factory=dict)
    cooldown_until: float = 0.0
    consecutive_failures: int = 0

    def supports_model(self, model: str | None) -> bool:
        return not model or not self.models or model in self.models

    def is_available(self, now: float) -> bool:
        return now >= self.cooldown_until


class AccountManager:
    def __init__(
        self,
        accounts: Iterable[Account],
        time_fn: Callable[[], float] | None = None,
    ) -> None:
        self._accounts = list(accounts)
        self._time_fn = time_fn or monotonic
        self._cursor = 0
        if not self._accounts:
            raise ValueError("at least one account is required")

    @property
    def accounts(self) -> list[Account]:
        return self._accounts

    def next_account(self, model: str | None = None, excluded_names: set[str] | None = None) -> Account:
        excluded_names = excluded_names or set()
        now = self._time_fn()
        for offset in range(len(self._accounts)):
            index = (self._cursor + offset) % len(self._accounts)
            account = self._accounts[index]
            if account.name in excluded_names:
                continue
            if not account.supports_model(model):
                continue
            if not account.is_available(now):
                continue
            self._cursor = (index + 1) % len(self._accounts)
            return account
        raise RuntimeError(f"no available account for model={model!r}")

    def mark_failure(self, account_name: str, cooldown_seconds: float) -> None:
        account = self._find(account_name)
        account.consecutive_failures += 1
        account.cooldown_until = self._time_fn() + cooldown_seconds

    def mark_success(self, account_name: str) -> None:
        account = self._find(account_name)
        account.consecutive_failures = 0
        account.cooldown_until = 0.0

    def _find(self, account_name: str) -> Account:
        for account in self._accounts:
            if account.name == account_name:
                return account
        raise KeyError(f"unknown account: {account_name}")

