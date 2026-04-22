#!/usr/bin/env bash

curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer anything" \
  -d '{
    "model": "minimax",
    "messages": [
      {"role": "user", "content": "Say hello from curl."}
    ]
  }'
