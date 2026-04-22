# TikTok Launch Pack

## Positioning

Do not pitch this as “buy tokens”.

Pitch it as:

- a dev tool that prevents API call failures
- a cheaper and easier way to test OpenAI-compatible apps
- a quick path to run free `kimi` / `minimax` calls after registration

## Video 1

### Hook

Your AI app breaks the moment one API key hits `429`?

### Script

I built a small OpenAI-compatible proxy manager that fixes exactly that.

It rotates across multiple API keys, retries automatically on `429`, and can switch proxies if one route becomes unstable.

Best part: your app still talks to one OpenAI-style `/v1` endpoint.

If you want to test it fast, I linked the repo and the endpoint I used to get free `kimi` and `minimax` access.

### Caption

OpenAI-compatible proxy + multi-account failover + free model testing. Repo in bio.

## Video 2

### Hook

Indie hackers do not need a giant AI platform for this.

### Script

Most people just need:

- multiple API keys
- one stable endpoint
- auto failover when rate limits hit

So I built the smaller version.

It is a self-hosted API manager for OpenAI-compatible requests with key rotation, proxy support, and model-based routing.

I also included an easy quickstart path with free `kimi` and `minimax`.

### Caption

Smaller than a full LLMOps stack. More useful for solo builders.

## Video 3

### Hook

Here is how I test OpenAI-compatible APIs for free before paying for scale.

### Script

Step 1: use a provider with OpenAI-compatible access.  
Step 2: register and get a key.  
Step 3: point a proxy manager at that base URL.  
Step 4: route requests by model and fail over when one account gets rate limited.

That is the workflow this repo is built around.

### Caption

Free first call, then scale later. Better than wiring every provider by hand.

## Bio Line

Build AI apps cheaper: free model access + open-source proxy manager

## CTA

- primary CTA: repo in bio
- secondary CTA: get free API access, then test the proxy
