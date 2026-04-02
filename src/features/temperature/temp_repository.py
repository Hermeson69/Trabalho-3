from sqlalchemy import select
from .temp_model import LeituraModel
from .temp_schema import LeituraCreateSchema, LeituraResponseSchema

class LeituraRepository:
    """Repository for managing LeituraModel database operations"""

    @staticmethod
    async def create_leitura(session, leitura_data: LeituraCreateSchema) -> LeituraModel:
        """Create a new leitura record in the database"""
        # add idempotencia check here if necessary
        existente_leitura = await session.get(LeituraModel, leitura_data.id)
        if existente_leitura:
            return existente_leitura
        nova_leitura = LeituraModel(
            id=leitura_data.id,
            sensor_id=leitura_data.sensor_id,
            temperatura=leitura_data.temperatura,
            timestamp=leitura_data.timestamp,  # will be set by the database default
        )
        session.add(nova_leitura)
        await session.commit()
        await session.refresh(nova_leitura)
        return nova_leitura
    
    @staticmethod
    async def logic_temp_response(leitura: LeituraModel) -> LeituraResponseSchema:
        """Convert a LeituraModel instance to a LeituraResponseSchema"""
        if(leitura.temperatura < 25):
            leitura.status_logico = "Normal"
        elif(leitura.temperatura >= 25 and leitura.temperatura < 30):
            leitura.status_logico = "Alerta"
        else:
            leitura.status_logico = "Perigo"
        return LeituraResponseSchema.from_orm(leitura)

    @staticmethod
    async def get_leitura_by_id(session, leitura_id: str) -> LeituraModel | None:
        """Retrieve a leitura record by its ID"""
        return await session.get(LeituraModel, leitura_id)


    @staticmethod
    async def get_all_leituras(session) -> list[LeituraModel]:
        """Retrieve all leitura records from the database"""
        result = await session.execute(select(LeituraModel))
        return result.scalars().all()