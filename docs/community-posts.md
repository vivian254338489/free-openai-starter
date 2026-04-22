# Community Post Pack

## Reddit Post

### Title

I built a lightweight OpenAI-compatible multi-account proxy manager with 429 retry and proxy rotation

### Body

I kept hitting the same problem with OpenAI-compatible integrations:

- one key gets rate limited
- one upstream gets unstable
- one region starts failing
- and then every app above it breaks

So I built a smaller self-hosted proxy manager focused on:

- multi-account API key rotation
- automatic retry on `429`
- proxy rotation
- model-aware routing
- OpenAI-compatible `/v1` forwarding

It is inspired by larger gateway projects, but the goal here is a more developer-first and easier-to-understand setup for indie builders and students.

Repo includes tests, config examples, Docker support, and a simple quickstart.

## Hacker News Post

### Title

Show HN: OpenAI-Compatible Multi-Account Proxy API Manager

### Body

Built a lightweight OpenAI-compatible proxy manager for a practical problem:

keeping apps alive when API keys get rate limited or upstream paths become unstable.

Core features:

- multi-account key pool
- automatic 429 retry + failover
- proxy rotation
- model-aware routing

Inspired by bigger LLM gateway projects, but intentionally narrower and easier to self-host.

## Product Hunt Tagline

OpenAI-compatible proxy manager with key rotation, 429 retry, and proxy failover

## Product Hunt Description

A lightweight self-hosted API manager for OpenAI-compatible workloads. Route by model, rotate across accounts, survive `429` errors, and switch proxies automatically.
