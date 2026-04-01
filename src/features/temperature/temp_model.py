from datetime import datetime
from sqlalchemy import Column, DateTime, Float, String, func
from src.core import BaseModel
from src.shared import IDGenerator


class LeituraModel(BaseModel):
    """
    Model for sensor readings
    """

    __tablename__ = "leitura"

    id = Column(String, primary_key=True, default=IDGenerator.generate_id)
    sensor_id = Column(String, nullable=False)
    temperatura = Column(Float, nullable=False)
    status_logico = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


