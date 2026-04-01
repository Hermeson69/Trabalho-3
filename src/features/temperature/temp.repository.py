from sqlalchemy import select
from .temp_model import LeituraModel
from .temp_schema import LeituraSchema, LeituraResponseSchema

class LeituraRepository:
    """Repository for managing LeituraModel database operations"""

    @staticmethod
    async def create_leitura(session, leitura_data: LeituraSchema) -> LeituraModel:
        """Create a new leitura record in the database"""
        nova_leitura = LeituraModel(
            sensor_id=leitura_data.sensor_id,
            temperatura=leitura_data.temperatura,
            status_logico=leitura_data.status_logico,
            timestamp=leitura_data.timestamp
        )
        session.add(nova_leitura)
        await session.commit()
        await session.refresh(nova_leitura)
        return nova_leitura

    @staticmethod
    async def get_leitura_by_id(session, leitura_id: str) -> LeituraModel | None:
        """Retrieve a leitura record by its ID"""
        return await session.get(LeituraModel, leitura_id)


    @staticmethod
    async def get_all_leituras(session) -> list[LeituraModel]:
        """Retrieve all leitura records from the database"""
        result = await session.execute(select(LeituraModel))
        return result.scalars().all()

    