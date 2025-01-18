from sqlmodel import SQLModel
from typing import Optional


class SpeakerCreate(SQLModel):
    name: str
    bio: str

class SpeakerRead(SQLModel):
    id: Optional[int]
    name: str
    bio: str