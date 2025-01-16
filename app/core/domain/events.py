from datetime import datetime
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class EventBase(SQLModel):
    name: str = Field(title="Conferencia de Tecnología")
    description: str = Field(title="Una conferencia sobre las últimas tendencias tecnológicas.")
    date: datetime = Field(title="2023-10-15T09:00:00")
    location: str = Field(title="Centro de Convenciones, Ciudad de México")

class EventCreate(EventBase):
    pass

class Event(EventBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Clave primaria
    attendees: List["Attendee"] = Relationship(back_populates="event")  # Relación con Attendee
    resources: List["Resource"] = Relationship(back_populates="event")  # Relación con Resource
    sessions: List["Session"] = Relationship(back_populates="event")  # Relación con Session
    speakers: List["Speaker"] = Relationship(back_populates="event")  # Relación con Speaker

class EventResponse(EventBase):
    id: int  # Clave primaria
    attendees: List["Attendee"] = []  # Lista de asistentes
    resources: List["Resource"] = []  # Lista de recursos
    sessions: List["Session"] = []  # Lista de sesiones
    speakers: List["Speaker"] = []  # Lista de ponentes