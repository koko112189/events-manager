from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from app.core.domain.attendee import Attendee
from app.core.domain.resource import Resource

class EventBase(BaseModel):
    name: str = Field(example="Conferencia de Tecnología")
    description: str = Field(example="Una conferencia sobre las últimas tendencias tecnológicas.")
    date: datetime = Field(example="2023-10-15T09:00:00")
    location: str = Field(example="Centro de Convenciones, Ciudad de México")

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

    class Config:
        from_attributes = True

class EventResponse(Event):
    attendees: List["Attendee"] = []
    resources: List["Resource"] = []

    class Config:
        from_attributes = True