from pydantic import BaseModel, Field

class SpeakerBase(BaseModel):
    name: str = Field(..., example="Juan Pérez")
    bio: str = Field(..., example="Experto en desarrollo de APIs con FastAPI.")
    event_id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        from_attributes = True  # Habilita la compatibilidad con ORM