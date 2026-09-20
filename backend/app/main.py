from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import close_client
from app.routers import admin, attiva_licenza, webhooks_opennode, webhooks_stripe


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield
    await close_client()


app = FastAPI(title="PH Backend", lifespan=lifespan)

app.include_router(webhooks_stripe.router)
app.include_router(webhooks_opennode.router)
app.include_router(attiva_licenza.router)
app.include_router(admin.router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
