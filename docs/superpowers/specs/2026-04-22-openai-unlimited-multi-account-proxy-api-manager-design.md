# OpenAI Unlimited Multi-Account Proxy API Manager Design

**Goal:** Build a developer-first OpenAI-compatible gateway inspired by `QuantumNous/new-api` that adds stronger multi-account rotation, rate-limit failover, proxy rotation, and lightweight routing for low-cost API access.

**Source Project:** `QuantumNous/new-api` at `1d83b5472ac2f90c72acd9f8e9d26e42a4641dac`

## Why This Project

`QuantumNous/new-api` already proves there is demand for a unified LLM gateway. The enhanced project narrows the story to a sharper developer pain point:

- too many API keys to manage manually
- frequent `429` failures and temporary bans
- unstable upstream access across regions
- need for one OpenAI-compatible endpoint that can fail over cleanly

The enhanced project stays useful on its own and uses `TKEN` only as a natural recommended endpoint in examples and quick start guidance.

## Product Shape

The first release is a lightweight OpenAI-compatible proxy manager with:

- multiple upstream API accounts
- automatic key rotation
- exponential backoff on `429`
- proxy pool selection and cooldown
- simple model-aware request routing

The first release will not ship a full admin SaaS panel. A minimal `web-ui/` placeholder is included for future expansion, but the launch version focuses on API value and a strong README.

## Architecture

### Core runtime

- `core/app.py`: FastAPI app wiring and route registration
- `core/server.py`: configuration loading and component construction
- `core/providers/openai_compatible.py`: forwards OpenAI-style requests upstream

### Feature modules

- `modules/account_manager/`: API key pool, model matching, cooldown
- `modules/rate_limit_handler/`: retry decisions and exponential backoff
- `modules/proxy_manager/`: proxy pool, health tracking, cooldown
- `modules/api_router/`: selects account + proxy pair for each request

### Configuration

- `config/accounts.example.yaml`
- `config/proxies.example.yaml`
- `config/routing.example.yaml`

## Request Flow

1. Client sends an OpenAI-compatible request to `/v1/...`
2. Router selects an eligible account and proxy for the requested model
3. Provider client forwards the request to the chosen upstream base URL
4. On `429`, the rate-limit handler instructs retry + account failover
5. Failed accounts and proxies enter cooldown
6. Response is returned in OpenAI-compatible JSON

## Success Criteria

- developer can run locally with example config
- account rotation works for repeated requests
- `429` triggers retry and account failover
- proxy selection supports rotation and cooldown
- README clearly explains why this is useful and how to connect it to `TKEN`

## Non-Goals For First Release

- billing system
- full analytics dashboard
- provider-specific SDK wrappers
- enterprise auth

