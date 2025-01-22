from sqlmodel import SQLModel
from typing import Optional


class SpeakerCreate(SQLModel):
    name: str
    bio: str
    session_id: Optional[int]

class SpeakerRead(SQLModel):
    id: Optional[int]
    name: str
    bio: str