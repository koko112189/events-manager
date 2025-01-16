from sqlmodel import SQLModel
from typing import Optional


class ResourceCreate(SQLModel):
    name: str
    description: str

class ResourceRead(SQLModel):
    id: Optional[str]
    name: str
    description: str