"""Connessione a MongoDB, creata in modo lazy.

Il client viene creato solo alla prima richiesta di accesso al DB, così
l'applicazione parte e /health risponde anche senza MONGODB_URI.
"""

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from app.config import get_settings

_client: AsyncMongoClient | None = None


def get_client() -> AsyncMongoClient:
    global _client
    if _client is None:
        uri = get_settings().mongodb_uri
        if not uri:
            raise RuntimeError("MONGODB_URI non configurata")
        _client = AsyncMongoClient(uri)
    return _client


def get_database() -> AsyncDatabase:
    # Il nome del DB è quello indicato nella URI di connessione.
    return get_client().get_default_database()


async def close_client() -> None:
    global _client
    if _client is not None:
        await _client.close()
        _client = None
