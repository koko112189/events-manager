from sqlmodel import SQLModel
from typing import Optional


class ResourceCreate(SQLModel):
    name: str
    description: str
    type: str
    event_id: Optional[int]
    session_id: Optional[int]

class ResourceRead(SQLModel):
    id: Optional[int]
    name: str
    description: str