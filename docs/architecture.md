# Architecture

## Overview

The runtime is a compact OpenAI-compatible forwarding layer built around four focused modules:

- `account_manager`: selects usable upstream accounts
- `proxy_manager`: selects a usable network path
- `rate_limit_handler`: decides retry, cooldown, and failover rules
- `api_router`: combines account + proxy selection into one route

## Request Lifecycle

1. Request arrives at `/v1/{path}`
2. Model name is extracted from the JSON body
3. `ApiRouter` chooses an account and optional proxy
4. `OpenAICompatibleProxyClient` forwards the request upstream
5. `RateLimitHandler` reacts to `429` or retryable server errors
6. Failed accounts and proxies are temporarily cooled down
7. Next attempt uses the next viable route

## Why This Shape

The project is intentionally smaller than a full LLMOps platform. The goal is to ship a gateway that is:

- understandable in one sitting
- easy to self-host
- easy to adapt to low-cost OpenAI-compatible providers

