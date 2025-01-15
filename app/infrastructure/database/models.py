from typing import List
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

