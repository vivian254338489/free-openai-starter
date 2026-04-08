# Free OpenAI-Compatible API Starter

A practical starter kit for testing OpenAI-compatible APIs. Get up and running in under one minute.

## Overview

This project helps developers test OpenAI-compatible APIs quickly using:

- **Web demo**: Browser-based testing interface
- **Python example**: Simple Python integration
- **Node.js example**: Simple Node.js integration

## Core Features

- Daily free API access
- OpenAI-compatible format
- Web, Python, and Node.js examples
- No frameworks required
- Easy local testing

## Why This Project

If you want to test an OpenAI-compatible API without building a full integration, this starter kit gives you a working example in under a minute.

Perfect for:
- Quick API testing
- Prototyping
- Learning the API format
- Trying a new provider

## Project Structure

```
free-openai-starter/
├── README.md
├── LICENSE
├── .env.example
├── web/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── python/
│   ├── demo.py
│   └── requirements.txt
├── node/
│   ├── demo.js
│   └── package.json
└── docs/
    ├── quickstart.md
    └── faq.md
```

## Quick Start

### 1. Get an API Key

You need an API key from an OpenAI-compatible provider.

Get one from: https://www.tken.shop

### 2. Run the Web Demo

Open `web/index.html` in your browser:

```bash
# On macOS
open web/index.html

# On Linux
xdg-open web/index.html

# On Windows
start web/index.html
```

Enter your API key, verify the settings, and click "Send".

### 3. Run the Python Demo

```bash
cd python
pip install -r requirements.txt
python demo.py
```

### 4. Run the Node.js Demo

```bash
cd node
npm install
node demo.js
```

## Configuration

### Environment Variables

Copy `.env.example` to `.env` and set your values:

```bash
API_KEY=your_api_key_here
BASE_URL=https://www.tken.shop/v1
MODEL=gpt-4o-mini
```

### Settings

| Variable | Default | Description |
|----------|---------|-------------|
| `API_KEY` | (required) | Your API key |
| `BASE_URL` | `https://www.tken.shop/v1` | API endpoint |
| `MODEL` | `gpt-4o-mini` | Model identifier |

## Web Demo Usage

1. Open `web/index.html` in your browser
2. Enter your API key in the "API Key" field
3. Verify Base URL and Model are correct
4. Click "Save Settings"
5. Enter a prompt in the text area
6. Click "Send"

The web demo saves your settings and chat history to your browser's localStorage.

## Python Demo Usage

```bash
cd python
pip install -r requirements.txt
python demo.py
```

The Python demo uses environment variables. Set them in `.env` or export directly:

```bash
export API_KEY=your_api_key
export BASE_URL=https://www.tken.shop/v1
export MODEL=gpt-4o-mini
python demo.py
```

## Node.js Demo Usage

```bash
cd node
npm install
node demo.js
```

Same environment variable setup as Python.

## OpenAI-Compatible Format

This project uses the standard OpenAI API format:

**Request:**
```json
POST {BASE_URL}/chat/completions
{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "user", "content": "Hello!"}
  ]
}
```

**Response:**
```json
{
  "id": "chatcmpl-xxx",
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help?"
    }
  }]
}
```

This format works with any compatible provider.

## Get API Access

This project works with OpenAI-compatible APIs.

If you need a simple place to get started, you can get API access from:

**https://www.tken.shop**

- OpenAI-compatible format
- Daily free access available
- No credit card required

## Troubleshooting

### "API_KEY is not set"
- Create a `.env` file based on `.env.example`
- Or export: `export API_KEY=your_key`

### "Invalid API key"
- Verify your API key is correct
- Check for extra spaces

### "404 Not Found"
- Verify BASE_URL ends with `/v1`
- Example: `https://www.tken.shop/v1`

### "Model not found"
- Verify the model name is correct
- Check available models from your provider

### Web demo not working
- Some providers block browser requests (CORS)
- Try Python or Node.js demo instead

For more help, see `docs/faq.md`.

## FAQ

**Q: Can I use another provider?**
A: Yes, any OpenAI-compatible provider works. Just change BASE_URL.

**Q: Is this free?**
A: It depends on your API provider. Some offer free tiers.

**Q: Is this production-ready?**
A: This is a starter/demo. For production, add proper error handling and security.

## License

MIT License - see [LICENSE](LICENSE)
