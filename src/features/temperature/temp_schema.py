from datetime import datetime
from pydantic import BaseModel


class LeituraCreateSchema(BaseModel):
    """Schema for creating a new sensor reading"""
    sensor_id: str
    temperatura: float


class LeituraResponseSchema(BaseModel):
    """Sensor reading response schema"""
    id: str
    sensor_id: str
    temperatura: float
    status_logico: str
    timestamp: datetime
    created_at: datetime

    class Config:
        from_attributes = True
