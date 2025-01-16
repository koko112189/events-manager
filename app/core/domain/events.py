from sqlmodel import SQLModel
from typing import Optional


class EventCreate(SQLModel):
    name: str
    date: str

class EventRead(SQLModel):
    id: Optional[str]
    name: str
    date: str