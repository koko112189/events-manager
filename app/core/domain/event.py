from datetime import datetime
from pydantic import BaseModel

class Event(BaseModel):
    id: str
    name: str
    description: str
    date: datetime
    location: str