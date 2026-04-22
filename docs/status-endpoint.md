# Status Endpoint

The project exposes a read-only runtime inspection endpoint:

```text
GET /healthz/details
```

## What It Returns

- account names
- configured model filters
- whether each account is currently available
- cooldown remaining seconds
- proxy status
- retry policy settings

## Why It Matters

This makes the proxy manager easier to debug in real use:

- see when an account is in cooldown
- check whether a proxy is still available
- confirm retry settings without opening config files

## Example

```json
{
  "accounts": [
    {
      "name": "tken-kimi-free",
      "available": true,
      "cooldown_remaining_seconds": 0.0
    }
  ],
  "proxies": [],
  "retry_policy": {
    "max_attempts": 3,
    "base_backoff_seconds": 0.5,
    "cooldown_seconds": 20.0
  }
}
```