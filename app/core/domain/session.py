from sqlmodel import SQLModel
from typing import Optional


class SessionCreate(SQLModel):
    name: str
    description: str
    start_time: str
    end_time: str

class SessionRead(SQLModel):
    id: Optional[str]
    name: str
    description: str
    start_time: str
    end_time: str