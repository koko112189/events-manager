from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class ResourceBase(SQLModel):
    name: str
    description: str
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")  # Clave foránea

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Clave primaria
    event: Optional["Event"] = Relationship(back_populates="resources")  # Relación con Event

class ResourceResponse(ResourceBase):
    id: int  # Clave primaria