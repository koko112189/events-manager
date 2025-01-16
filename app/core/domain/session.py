from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class SessionBase(SQLModel):
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")  # Clave foránea
    speaker_id: Optional[int] = Field(default=None, foreign_key="speaker.id")  # Clave foránea

class SessionCreate(SessionBase):
    pass

class Session(SessionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Clave primaria
    event: Optional["Event"] = Relationship(back_populates="sessions")  # Relación con Event
    speaker: Optional["Speaker"] = Relationship(back_populates="sessions")  # Relación con Speaker

class SessionResponse(SessionBase):
    id: int  # Clave primaria