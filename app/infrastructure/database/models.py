from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    name: str
    date: datetime
    sessions: List["Session"] = Relationship(back_populates="event")
    resources: List["Resource"] = Relationship(back_populates="event")
    attendees: List["Attendee"] = Relationship(back_populates="event")

    class Config:
        orm_mode = True

class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
    name: str
    capacity: int
    start_time: datetime
    end_time: datetime
    date: datetime
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")
    event: Optional[Event] = Relationship(back_populates="sessions")
    speaker: Optional["Speaker"] = Relationship(back_populates="sessions")
    resources: Optional["Resource"] = Relationship(back_populates="session")
    attendees: Optional["Attendee"] = Relationship(back_populates="session")

    class Config:
        orm_mode = True

class Speaker(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
    name: str
    bio: str
    session_id: Optional[int] = Field(default=None, foreign_key="session.id")
    sessions: List[Session] = Relationship(back_populates="speaker")

    class Config:
        orm_mode = True

class Resource(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 
    name: str
    type: str  # Puede ser "file", "link", "material", etc.
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")
    event: Optional[Event] = Relationship(back_populates="resources")
    session_id: Optional[int] = Field(default=None, foreign_key="session.id")
    session: Optional[Session] = Relationship(back_populates="resources")

    class Config:
        orm_mode = True

class Attendee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
    name: str
    email: str
    event_id: Optional[int] = Field(default=None, foreign_key="event.id")
    event: Optional[Event] = Relationship(back_populates="attendees")
    session_id: Optional[int] = Field(default=None, foreign_key="session.id")
    session: Optional[Session] = Relationship(back_populates="attendees")

    class Config:
        orm_mode = True
        