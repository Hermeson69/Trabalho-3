import asyncio

import uvicorn

from src.db.bd import init_db


def run() -> None:
    """Run the server with database initialization"""
    asyncio.run(init_db())
    uvicorn.run("src.api:app", host="0.0.0.0", port=8000, log_level="info")