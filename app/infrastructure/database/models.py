from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime
from pydantic import BaseModel, Field

class EventModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    description: str
    date: datetime
    location: str

    attendees: List["AttendeeModel"] = Relationship(back_populates="event")
    resources: List["ResourceModel"] = Relationship(back_populates="event")
    sessions: list["SessionModel"] = Relationship(back_populates="event")
    speakers: list["SpeakerModel"] = Relationship(back_populates="event")

class AttendeeModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    email: str
    event_id: str = Field(foreign_key="eventmodel.id")

    event: "EventModel" = Relationship(back_populates="attendees")


class ResourceModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    description: str
    event_id: str = Field(foreign_key="eventmodel.id")

    event: "EventModel" = Relationship(back_populates="resources")

class SessionModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    description: str
    start_time: datetime
    end_time: datetime
    event_id: str = Field(foreign_key="eventmodel.id")
    speaker_id: Optional[str] = Field(default=None, foreign_key="speakermodel.id")
    capacity: int

    # Relaciones
    event: "EventModel" = Relationship(back_populates="sessions")
    speaker: Optional["SpeakerModel"] = Relationship(back_populates="sessions")

class SpeakerModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    bio: str
    event_id: str = Field(foreign_key="eventmodel.id")
    # Relaciones
    event: "EventModel" = Relationship(back_populates="speakers")
    sessions: list["SessionModel"] = Relationship(back_populates="speaker")