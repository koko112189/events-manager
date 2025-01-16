from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class AttendeeBase(SQLModel):
    name: str
    email: str
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")  # Clave foránea

class AttendeeCreate(AttendeeBase):
    pass

class Attendee(AttendeeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Clave primaria
    event: Optional["Event"] = Relationship(back_populates="attendees")  # Relación con Event

class AttendeeResponse(AttendeeBase):
    id: int  # Clave primaria