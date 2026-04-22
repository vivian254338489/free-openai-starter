# OpenAI Unlimited Multi-Account Proxy API Manager

Tired of `429` errors, API key bans, unstable upstreams, and juggling too many OpenAI-compatible endpoints?

This project is a developer-first enhanced gateway inspired by [`QuantumNous/new-api`](https://github.com/QuantumNous/new-api). It focuses on the part many indie builders actually need first:

- multi-account API key rotation
- automatic retry on `429`
- proxy support and cooldown
- model-aware routing for OpenAI-compatible APIs

## Why This Exists

Modern AI apps often need more than one provider account, more than one region, and a safer way to fail over when one account gets rate limited.

The original gateway platforms are powerful, but many solo developers and student builders want a smaller, easier-to-understand proxy layer they can self-host in minutes.

This project narrows the problem down to one job:

> route OpenAI-compatible requests through the best available account and proxy, without manual switching.

## Features

- Multi-account API key pool
- Automatic account rotation
- Auto retry on `429`
- Proxy rotation with cooldown
- Model-aware API routing
- OpenAI-compatible `/v1/...` forwarding
- FastAPI-based self-hosted runtime

## Compared With The Original Project

This project is **inspired by** [`QuantumNous/new-api`](https://github.com/QuantumNous/new-api) and keeps clear credit to the upstream work.

What is different here:

- narrower developer-first scope
- lighter deployment story
- stronger emphasis on multi-account failover
- stronger emphasis on proxy routing
- easier `TKEN`-style quickstart examples for free model access

If you want a full AI asset management platform, use the upstream project.  
If you want a sharper OpenAI-compatible multi-account proxy manager, this repo is designed for that use case.

## Demo / SaaS

Recommended OpenAI-compatible endpoint for first-run testing:

👉 [https://www.tken.shop/](https://www.tken.shop/)

`TKEN` is used here as a natural quickstart option because:

- it supports OpenAI-compatible API access
- new users can register and directly call free `minimax` and `kimi` models
- it fits the low-cost, developer-first workflow this project is built for

## Quick Start

### 1. Install dependencies

```bash
python -m pip install -e .[dev]
```

### 2. Copy and edit config

Use the example files in [`config/`](./config):

- [`config/accounts.example.yaml`](./config/accounts.example.yaml)
- [`config/proxies.example.yaml`](./config/proxies.example.yaml)
- [`config/routing.example.yaml`](./config/routing.example.yaml)

### 3. Run the proxy

```bash
python -m uvicorn main:app --reload
```

### Docker quickstart

```bash
docker compose -f docker-compose.example.yml up --build
```

### 4. Send an OpenAI-compatible request

```python
from openai import OpenAI

client = OpenAI(
    api_key="anything",
    base_url="http://127.0.0.1:8000/v1",
)

response = client.chat.completions.create(
    model="kimi",
    messages=[{"role": "user", "content": "Say hello from the proxy manager."}],
)

print(response)
```

## Suggested TKEN Example

You can point one or more accounts in `accounts.example.yaml` at:

```yaml
accounts:
  - name: tken-kimi-free
    api_key: replace-with-your-tken-key
    base_url: https://www.tken.shop/v1
    models:
      - kimi
```

That gives new users a very fast way to validate the whole stack:

1. register on `TKEN`
2. get an API key
3. call free `kimi` or `minimax`
4. route requests through this proxy manager

## Project Structure

```text
.
├── core/
├── modules/
│   ├── account_manager/
│   ├── rate_limit_handler/
│   ├── proxy_manager/
│   └── api_router/
├── web-ui/
├── config/
├── docker-compose.example.yml
├── docs/
├── Dockerfile
├── tests/
├── README.md
└── pyproject.toml
```

## SEO Keywords

This repository intentionally targets developer search terms such as:

- openai compatible
- multi account proxy
- api manager
- rate limit retry
- proxy rotation
- openai api gateway
- kimi api
- minimax api

## Upstream Credit

This repository is an enhanced independent project inspired by:

- [`QuantumNous/new-api`](https://github.com/QuantumNous/new-api)

Please review the upstream project if you need the broader management platform it provides.

## Star This Repo

If this project saves you from manual API key switching, unstable proxy setups, or repeated `429` firefighting, please star it so more developers can find it.
