from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .temp_repository import LeituraRepository
from .temp_schema import LeituraCreateSchema, LeituraResponseSchema
from .temp_model import LeituraModel


class LeituraService:
    """Service layer for managing LeituraModel operations"""

    @staticmethod
    async def create_leitura(session: AsyncSession, leitura_data: LeituraCreateSchema) -> LeituraResponseSchema:
        """Create a new leitura and return the response schema"""
        nova_leitura = await LeituraRepository.create_leitura(session, leitura_data)
        return await LeituraRepository.logic_temp_response(nova_leitura)

    @staticmethod
    async def get_leitura_by_id(session: AsyncSession, leitura_id: str) -> LeituraResponseSchema:
        """Retrieve a leitura by ID and return the response schema"""
        leitura = await LeituraRepository.get_leitura_by_id(session, leitura_id)
        if not leitura:
            raise HTTPException(status_code=404, detail="Leitura not found")
        return await LeituraRepository.logic_temp_response(leitura)

    @staticmethod
    async def get_all_leituras(session: AsyncSession) -> list[LeituraResponseSchema]:
        """Retrieve all leituras and return a list of response schemas"""
        leituras = await LeituraRepository.get_all_leituras(session)
        return [await LeituraRepository.logic_temp_response(leitura) for leitura in leituras]

    @staticmethod
    async def logic_temp_response(leitura: LeituraModel) -> LeituraResponseSchema:
        """Convert a LeituraModel instance to a LeituraResponseSchema with logic status"""
        if leitura.temperatura < 25:
            leitura.status_logico = "Normal"
        elif 25 <= leitura.temperatura < 30:
            leitura.status_logico = "Alerta"
        else:
            leitura.status_logico = "Perigo"
        return LeituraResponseSchema.from_orm(leitura)