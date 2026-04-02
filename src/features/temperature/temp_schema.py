from datetime import datetime
from pydantic import BaseModel


class LeituraCreateSchema(BaseModel):
    """Schema for creating a new sensor reading"""
    id: str
    sensor_id: str
    temperatura: float
    timestamp: datetime


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