from datetime import datetime
from pydantic import BaseModel


class LeituraSchema(BaseModel):
    """Sensor reading schema"""
    sensor_id: str
    temperatura: float
    status_logico: str
    timestamp: datetime


class LeituraResponseSchema(LeituraSchema):
    """Sensor reading response schema"""
    id: str
    created_at: datetime

    class Config:
        from_attributes = True


