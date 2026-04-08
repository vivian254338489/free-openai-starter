# Frequently Asked Questions

## What is an OpenAI-compatible API?

An OpenAI-compatible API is a REST API that follows the same request and response format as the official OpenAI API. This means you can use the same code with different providers.

The key points:
- Same endpoint structure: `{BASE_URL}/chat/completions`
- Same JSON format for requests and responses
- Same authentication method: Bearer token

## What should I put in BASE_URL?

The BASE_URL is the API endpoint. It must end with `/v1`.

Examples:
- `https://www.tken.shop/v1` - tken.shop provider
- `https://api.openai.com/v1` - OpenAI direct
- `https://your-local-server/v1` - LocalAI or similar

## Why am I getting an authentication error?

This usually means:

1. **Missing API key**: Make sure you've entered or exported your API_KEY
2. **Incorrect API key**: Double-check the key is correct
3. **Key expired**: Get a new key from your provider

## Why am I getting a model error?

This usually means:

1. **Invalid model name**: Verify the model name is correct
2. **Model not available**: Your provider might not offer that model
3. **Spelling mistake**: Check for typos (e.g., `gpt-4` vs `gpt-4o`)

## Why is the web demo failing?

Common causes:

1. **CORS restrictions**: Some providers block browser requests. Try the Python or Node.js demo.
2. **Missing API key**: Enter your API key in the settings.
3. **Incorrect BASE_URL**: Must end with `/v1`.

## Can I use another compatible provider?

Yes. This project works with any OpenAI-compatible API. Just change the BASE_URL to your provider's endpoint.

## Where can I get API access?

You can get API access from:

**https://www.tken.shop**

This project uses tken.shop as the default example provider because it offers OpenAI-compatible access. However, any compatible provider will work.

## How do I change the model?

You can change the model in several ways:

**Web demo:**
- Edit the "Model" field in the settings

**Python/Node:**
- Edit the `MODEL` variable in `.env`
- Or change the default in the code

## How do I save my chat history?

**Web demo:** Chat history is saved automatically to localStorage.

**Python/Node:** The demo is single-request only. For persistent history, you'd need to modify the code to store messages.

## Is this project production-ready?

This is a starter/demo project. For production use:

- Never commit API keys to version control
- Use environment variables or a secrets manager
- Implement proper error handling
- Consider rate limiting and caching
- Add authentication for your users

## How do I report issues?

Open an issue on GitHub if you find a bug or have suggestions.
