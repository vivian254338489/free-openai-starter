from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from core.providers.openai_compatible import OpenAICompatibleProxyClient


def create_app(client: OpenAICompatibleProxyClient) -> FastAPI:
    app = FastAPI(title="OpenAI Unlimited Multi-Account Proxy API Manager")

    @app.get("/healthz")
    async def healthz() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/healthz/details")
    async def healthz_details() -> dict[str, Any]:
        return client.status_snapshot()

    @app.get("/version")
    async def version() -> dict[str, str]:
        return {"version": "0.1.0"}

    @app.post("/v1/{path:path}")
    async def forward_request(path: str, body: dict[str, Any]) -> JSONResponse:
        status_code, payload = await client.forward(f"v1/{path}", body)
        return JSONResponse(status_code=status_code, content=payload)

    return app
