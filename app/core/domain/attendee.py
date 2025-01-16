from sqlmodel import SQLModel
from typing import Optional


class AttendeeCreate(SQLModel):
    name: str
    email: str
    event_id: Optional[str]

class AttendeeRead(SQLModel):
    id: Optional[str]
    name: str
    email: str