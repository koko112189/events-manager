from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class SpeakerBase(SQLModel):
    name: str
    bio: str
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")  # Clave foránea

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Clave primaria
    event: Optional["Event"] = Relationship(back_populates="speakers")  # Relación con Event
    sessions: List["Session"] = Relationship(back_populates="speaker")  # Relación con Session

class SpeakerResponse(SpeakerBase):
    id: int  # Clave primaria