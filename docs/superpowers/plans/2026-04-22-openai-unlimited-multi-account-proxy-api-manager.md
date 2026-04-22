# OpenAI Unlimited Multi-Account Proxy API Manager Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a lightweight OpenAI-compatible API manager with multi-account rotation, rate-limit retry, proxy rotation, and model-aware routing.

**Architecture:** A small FastAPI gateway will compose four focused modules: account selection, proxy selection, retry policy, and request routing. The runtime will load YAML config, route OpenAI-style requests, and forward them upstream with retries and cooldowns.

**Tech Stack:** Python 3.11, FastAPI, httpx, PyYAML, pytest

---

### Task 1: Define tests for account rotation

**Files:**
- Create: `tests/test_account_manager.py`
- Create: `modules/account_manager/manager.py`

- [ ] Step 1: Write failing tests for round-robin and cooldown behavior
- [ ] Step 2: Run `pytest tests/test_account_manager.py -q` and confirm failure
- [ ] Step 3: Implement `Account` and `AccountManager`
- [ ] Step 4: Run `pytest tests/test_account_manager.py -q` and confirm pass

### Task 2: Define tests for proxy rotation

**Files:**
- Create: `tests/test_proxy_manager.py`
- Create: `modules/proxy_manager/manager.py`

- [ ] Step 1: Write failing tests for proxy rotation and cooldown behavior
- [ ] Step 2: Run `pytest tests/test_proxy_manager.py -q` and confirm failure
- [ ] Step 3: Implement `ProxyEndpoint` and `ProxyManager`
- [ ] Step 4: Run `pytest tests/test_proxy_manager.py -q` and confirm pass

### Task 3: Define tests for rate-limit retry policy

**Files:**
- Create: `tests/test_rate_limit_handler.py`
- Create: `modules/rate_limit_handler/retry.py`

- [ ] Step 1: Write failing tests for `429` retry decisions
- [ ] Step 2: Run `pytest tests/test_rate_limit_handler.py -q` and confirm failure
- [ ] Step 3: Implement `RetryPolicy`, `RetryDecision`, and `RateLimitHandler`
- [ ] Step 4: Run `pytest tests/test_rate_limit_handler.py -q` and confirm pass

### Task 4: Define tests for route selection

**Files:**
- Create: `tests/test_api_router.py`
- Create: `modules/api_router/router.py`

- [ ] Step 1: Write failing tests for account + proxy route selection
- [ ] Step 2: Run `pytest tests/test_api_router.py -q` and confirm failure
- [ ] Step 3: Implement `ApiRouter` and `RouteSelection`
- [ ] Step 4: Run `pytest tests/test_api_router.py -q` and confirm pass

### Task 5: Build the forwarding runtime

**Files:**
- Create: `core/providers/openai_compatible.py`
- Create: `core/app.py`
- Create: `core/server.py`
- Create: `config/accounts.example.yaml`
- Create: `config/proxies.example.yaml`
- Create: `config/routing.example.yaml`

- [ ] Step 1: Add provider client that uses router + retry policy
- [ ] Step 2: Add FastAPI endpoints for `/healthz` and `/v1/{path:path}`
- [ ] Step 3: Add YAML config loading and example config files
- [ ] Step 4: Run targeted tests and a smoke import check

### Task 6: Ship documentation and launch materials

**Files:**
- Create: `README.md`
- Create: `docs/architecture.md`
- Create: `docs/tken-integration.md`
- Create: `docs/deployment.md`
- Create: `web-ui/README.md`

- [ ] Step 1: Write a conversion-focused README with upstream credit
- [ ] Step 2: Add architecture and deployment docs
- [ ] Step 3: Document `TKEN` integration as a recommended endpoint

