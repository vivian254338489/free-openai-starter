from modules.rate_limit_handler.retry import RateLimitHandler, RetryPolicy


def test_rate_limit_handler_retries_and_switches_account_on_429() -> None:
    handler = RateLimitHandler(RetryPolicy(max_attempts=3, base_backoff_seconds=0.5, cooldown_seconds=10.0))

    first = handler.decision(status_code=429, attempt=1)
    assert first.should_retry is True
    assert first.switch_account is True
    assert first.cooldown_seconds == 10.0
    assert first.sleep_seconds == 0.5


def test_rate_limit_handler_stops_retrying_after_max_attempts() -> None:
    handler = RateLimitHandler(RetryPolicy(max_attempts=3, base_backoff_seconds=0.5, cooldown_seconds=10.0))

    last = handler.decision(status_code=429, attempt=3)
    assert last.should_retry is False
    assert last.switch_account is False
    assert last.sleep_seconds == 0.0

