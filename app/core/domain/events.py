from datetime import datetime
from pydantic import field_validator
from sqlmodel import SQLModel
from typing import Optional


class EventCreate(SQLModel):
    name: str
    date: datetime

    class Config:
        orm_mode = True
    # @field_validator("date", mode="before")
    # def validate_date(cls, value):
    #     if isinstance(value, str):
    #         return value  # Acepta directamente cadenas
    #     raise ValueError("El campo 'date' debe ser una cadena ISO 8601 (YYYY-MM-DDTHH:MM:SS).")

class EventRead(SQLModel):
    id: Optional[int]
    name: str
    date: datetime

    class Config:
        orm_mode = True