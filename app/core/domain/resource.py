# app/core/domain/resource.py
from pydantic import BaseModel, Field

from app.core.domain.event import Event

class ResourceBase(BaseModel):
    name: str = Field(..., example="Sala de Conferencias A")
    description: str = Field(..., example="Sala con capacidad para 100 personas.")
    event_id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

class ResourceCreate(ResourceBase):
    pass

class Resource(ResourceBase):
    id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        from_attributes = True  

class ResourceResponse(Resource):
    event: "Event"

    class Config:
        from_attributes = True