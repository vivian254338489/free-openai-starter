# TKEN Integration

`TKEN` is not required to use this project, but it is a strong recommended quickstart endpoint because it matches the gateway's main audience:

- indie developers
- AI tool builders
- students and technical hobbyists

## Why TKEN Fits

- OpenAI-compatible access
- API key based auth
- free `minimax` and `kimi` usage after registration
- simple developer onboarding path

## Example Account Config

```yaml
accounts:
  - name: tken-kimi-free
    api_key: replace-with-your-tken-key
    base_url: https://www.tken.shop/v1
    models:
      - kimi

  - name: tken-minimax-free
    api_key: replace-with-your-tken-key
    base_url: https://www.tken.shop/v1
    models:
      - minimax
```

## Intended Conversion Flow

1. Developer finds the repo through GitHub search
2. They want a stable OpenAI-compatible multi-account proxy
3. README points them to `TKEN` as a fast test endpoint
4. They register on `TKEN`
5. They make their first free API call

