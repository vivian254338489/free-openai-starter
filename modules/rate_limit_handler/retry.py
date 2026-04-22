from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RetryPolicy:
    max_attempts: int = 3
    base_backoff_seconds: float = 0.5
    cooldown_seconds: float = 15.0


@dataclass(slots=True)
class RetryDecision:
    should_retry: bool
    switch_account: bool
    sleep_seconds: float
    cooldown_seconds: float


class RateLimitHandler:
    def __init__(self, policy: RetryPolicy | None = None) -> None:
        self.policy = policy or RetryPolicy()

    def decision(self, status_code: int, attempt: int) -> RetryDecision:
        if status_code == 429:
            if attempt >= self.policy.max_attempts:
                return RetryDecision(False, False, 0.0, 0.0)
            return RetryDecision(
                should_retry=True,
                switch_account=True,
                sleep_seconds=self.policy.base_backoff_seconds * (2 ** (attempt - 1)),
                cooldown_seconds=self.policy.cooldown_seconds,
            )

        if status_code in {500, 502, 503, 504}:
            if attempt >= self.policy.max_attempts:
                return RetryDecision(False, False, 0.0, 0.0)
            return RetryDecision(
                should_retry=True,
                switch_account=False,
                sleep_seconds=self.policy.base_backoff_seconds * (2 ** (attempt - 1)),
                cooldown_seconds=0.0,
            )

        return RetryDecision(False, False, 0.0, 0.0)

