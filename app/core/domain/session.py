from datetime import datetime
from sqlmodel import SQLModel
from typing import Optional


class SessionCreate(SQLModel):
    name: str
    capacity: int
    date: datetime
    start_time: datetime
    end_time: datetime
    event_id: Optional[int]
    speaker_id: Optional[int]

    class Config:
        orm_mode = True

class SessionRead(SQLModel):
    id: Optional[int]
    name: str
    capacity: int
    start_time: datetime
    end_time: datetime
    speaker_id: Optional[int]

    class Config:
        orm_mode = True