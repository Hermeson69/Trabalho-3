from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core import BaseModel, settings

async_engine = create_async_engine(settings.database_url, echo=True)
async_sessionmaker = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    """Get an async database session"""
    async with async_sessionmaker() as session:
        yield session


async def init_db() -> None:
    """Initialize the database with all tables"""
    from src.features.temperature import LeituraModel

    async with async_engine.begin() as conn:
        print("Creating database tables...")
        await conn.run_sync(BaseModel.metadata.create_all)
        print("Database tables created successfully!")