from sqlmodel import SQLModel, Field
from datetime import datetime

class EventModel(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str
    description: str
    date: datetime
    location: str