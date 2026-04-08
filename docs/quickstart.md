# Quick Start Guide

This guide helps you test an OpenAI-compatible API in under one minute.

## Prerequisites

- An API key from an OpenAI-compatible provider
- A modern web browser (for the web demo)
- Python 3.8+ (for Python demo)
- Node.js 18+ (for Node.js demo)

## Step 1: Get an API Key

If you don't have an API key yet, you can get one from:

**https://www.tken.shop**

This project uses the OpenAI-compatible API format, so any compatible provider will work.

## Step 2: Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` with your API key:

```bash
API_KEY=your_api_key_here
BASE_URL=https://www.tken.shop/v1
MODEL=gpt-4o-mini
```

## Step 3: Run the Web Demo

The web demo is the fastest way to test your API:

1. Open `web/index.html` in your browser
2. Enter your API key
3. Verify Base URL and Model are correct
4. Click "Save Settings"
5. Enter a prompt and click "Send"

The web demo saves your settings and chat history to localStorage.

## Step 4: Run the Python Demo

```bash
cd python
pip install -r requirements.txt
python demo.py
```

## Step 5: Run the Node.js Demo

```bash
cd node
npm install
node demo.js
```

## Configuration Options

| Variable | Default | Description |
|----------|---------|-------------|
| `API_KEY` | (required) | Your API key |
| `BASE_URL` | `https://www.tken.shop/v1` | API endpoint |
| `MODEL` | `gpt-4o-mini` | Model to use |

## Troubleshooting

### "API_KEY is not set"

- Make sure you created a `.env` file
- Or export the variable directly: `export API_KEY=your_key`

### "Invalid API key"

- Verify your API key is correct
- Check for extra spaces in the key

### "404 Not Found"

- Verify BASE_URL ends with `/v1`
- Check the provider URL format

### "Model not found"

- Verify the model name is correct
- Check what models your provider offers

### Web demo not working

- Some API providers block browser requests (CORS)
- Try the Python or Node.js demo instead
- Or use a CORS proxy for testing

## Next Steps

- Try different prompts
- Experiment with temperature and other options
- Read the FAQ in `docs/faq.md`
- Build your own application
