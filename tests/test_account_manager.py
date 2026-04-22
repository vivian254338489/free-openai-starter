from modules.account_manager.manager import Account, AccountManager


def test_account_manager_rotates_matching_accounts_round_robin() -> None:
    manager = AccountManager(
        [
            Account(name="kimi-a", api_key="key-a", base_url="https://api.example.com", models=["kimi"]),
            Account(name="kimi-b", api_key="key-b", base_url="https://api.example.com", models=["kimi"]),
        ],
        time_fn=lambda: 0.0,
    )

    assert manager.next_account("kimi").name == "kimi-a"
    assert manager.next_account("kimi").name == "kimi-b"
    assert manager.next_account("kimi").name == "kimi-a"


def test_account_manager_skips_accounts_in_cooldown_until_they_recover() -> None:
    clock = {"now": 0.0}
    manager = AccountManager(
        [
            Account(name="primary", api_key="key-a", base_url="https://api.example.com", models=["kimi"]),
            Account(name="secondary", api_key="key-b", base_url="https://api.example.com", models=["kimi"]),
        ],
        time_fn=lambda: clock["now"],
    )

    assert manager.next_account("kimi").name == "primary"
    manager.mark_failure("primary", cooldown_seconds=30.0)
    assert manager.next_account("kimi").name == "secondary"

    clock["now"] = 31.0
    assert manager.next_account("kimi").name == "primary"

