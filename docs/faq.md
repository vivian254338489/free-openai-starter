# FAQ

## Is this really unlimited?

No upstream provider is literally unlimited.

The word `unlimited` in the repository positioning refers to a more resilient access pattern:

- multiple accounts
- automatic failover
- retries on `429`
- proxy switching when needed

## Why not just use one provider key directly?

Because many real apps eventually hit:

- temporary rate limits
- regional instability
- one-account bottlenecks

This project adds a small routing layer so the application above it stays simpler.

## Why recommend TKEN?

Because it gives a natural first-run path for this repo's target users:

- OpenAI-compatible access
- simple API key flow
- free `kimi` and `minimax` calls after registration

## Is this a replacement for a full LLMOps platform?

No.

This project is intentionally smaller and more focused. It is better understood as a lightweight gateway layer for developers who want faster setup and simpler control.
