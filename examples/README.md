# Examples

This directory contains simple clients that talk to the proxy manager through an OpenAI-compatible interface.

## Files

- `python/openai_client.py`
- `node/openai_client.mjs`
- `go/main.go`
- `curl/chat_completion.sh`

All of them assume your proxy is available at:

```text
http://127.0.0.1:8000/v1
```

## Run

### Python

```bash
pip install -r examples/python/requirements.txt
python examples/python/openai_client.py
```

### Node.js

```bash
cd examples/node
npm install
node openai_client.mjs
```

### Go

```bash
cd examples/go
go run .
```
