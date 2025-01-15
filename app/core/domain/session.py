from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class SessionBase(BaseModel):
    name: str = Field(..., example="Introducción a FastAPI")
    description: str = Field(..., example="Una sesión introductoria sobre FastAPI.")
    start_time: datetime = Field(..., example="2023-10-15T09:00:00")
    end_time: datetime = Field(..., example="2023-10-15T10:00:00")
    event_id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    speaker_id: Optional[str] = Field(None, example="123e4567-e89b-12d3-a456-426614174000")
    capacity: int = Field(..., example=100)

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        from_attributes = True  # Habilita la compatibilidad con ORM