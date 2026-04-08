#!/usr/bin/env python3
"""
Free OpenAI-Starter Python Demo

This script demonstrates how to call an OpenAI-compatible API
using the official OpenAI Python client.
"""

import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

API_KEY = os.getenv("API_KEY", "")
BASE_URL = os.getenv("BASE_URL", "https://www.tken.shop/v1")
MODEL = os.getenv("MODEL", "gpt-4o-mini")


def check_config():
    """Verify configuration."""
    if not API_KEY:
        print("Error: API_KEY is not set")
        print("Set it with: export API_KEY=your_api_key")
        print("Or create a .env file based on .env.example")
        sys.exit(1)


def main():
    check_config()

    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai package not installed")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    print(f"API: {BASE_URL}")
    print(f"Model: {MODEL}")
    print("-" * 40)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": "Say hello in one sentence."}
            ],
            max_tokens=50,
            temperature=0.7
        )

        print("Success!")
        print("-" * 40)
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens: {response.usage.total_tokens}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
