from pydantic import BaseModel, Field, EmailStr

from app.core.domain.event import Event

class AttendeeBase(BaseModel):
    name: str = Field(..., example="Juan Pérez")
    email: EmailStr = Field(..., example="juan.perez@example.com")
    event_id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

class AttendeeCreate(AttendeeBase):
    pass

class Attendee(AttendeeBase):
    id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        from_attributes = True 

class AttendeeResponse(Attendee):
    event: "Event"

    class Config:
        from_attributes = True 