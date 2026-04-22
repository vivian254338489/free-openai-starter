# GitHub Launch Pack

## Repository Title

OpenAI Unlimited Multi-Account Proxy API Manager

## Repository Description

OpenAI-compatible multi-account proxy API manager with 429 retry, API key rotation, proxy support, and model-aware routing.

## Topics

- ai-tools
- api-management
- proxy
- openai
- claude
- multi-account
- rate-limit
- openai-compatible
- api-gateway
- llm-proxy

## First Release Notes

### Short version

Built a lightweight OpenAI-compatible proxy manager inspired by `new-api`, focused on real developer pain:

- multi-account key pools
- automatic 429 recovery
- proxy rotation
- model-aware routing

Works well when you need a practical gateway layer instead of a full platform.

### Long version

This project is an independent enhanced gateway inspired by `QuantumNous/new-api`.

I wanted something narrower and more developer-first for indie builders running OpenAI-compatible workloads:

- rotate across multiple API keys
- survive `429` errors automatically
- swap proxies when access paths get unstable
- route requests by model with a smaller, easier-to-understand setup

The repo includes tested core modules, Docker support, config examples, and a quickstart path using an OpenAI-compatible endpoint.

## Pinned Comment For Early Users

If you try this repo, test the following first:

1. configure 2 accounts for the same model
2. force one into cooldown
3. verify failover works
4. verify your OpenAI SDK still works unchanged against `/v1`

