from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_async_session
from .temp_service import LeituraService
from .temp_schema import LeituraCreateSchema, LeituraResponseSchema

router = APIRouter(
    prefix="/leituras",
    tags=["Leituras"],
)


@router.post("/", response_model=LeituraResponseSchema)
async def create_leitura(
    leitura_data: LeituraCreateSchema,
    session: AsyncSession = Depends(get_async_session)
):
    """Create a new sensor reading"""
    return await LeituraService.create_leitura(session, leitura_data)


@router.get("/{leitura_id}", response_model=LeituraResponseSchema)
async def get_leitura(
    leitura_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    """Get a sensor reading by ID"""
    return await LeituraService.get_leitura_by_id(session, leitura_id)


@router.get("/", response_model=list[LeituraResponseSchema])
async def list_leituras(
    session: AsyncSession = Depends(get_async_session)
):
    """Get all sensor readings"""
    return await LeituraService.get_all_leituras(session)
