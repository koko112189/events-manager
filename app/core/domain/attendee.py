from sqlmodel import SQLModel
from typing import Optional


class AttendeeCreate(SQLModel):
    name: str
    email: str
    event_id: Optional[int]
    session_id: Optional[int]

class AttendeeRead(SQLModel):
    id: Optional[int]
    name: str
    email: str