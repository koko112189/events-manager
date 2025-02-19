from datetime import datetime
from typing import Type
from annotated_types import T
from sqlalchemy.orm import Session
from app.core.ports.event_repository import EventRepository
from app.core.domain.events import  EventCreate, EventRead
from app.infrastructure.database.models import Event as EventModel  

class PostgresEventRepository(EventRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, event: EventCreate) -> EventRead:
        new_event = EventModel(**event.dict())
        self.session.add(new_event)
        self.session.commit()
        self.session.refresh(new_event)
        return EventRead.from_orm(new_event)

    def find_by_id(self, event_id: int) -> EventRead:
        
        event_model = self.session.query(EventModel).filter(EventModel.id == event_id).first()
        if event_model:
            return EventRead(**event_model.dict())
        raise ValueError("Event not found")
    
    def list_events(self) -> list[EventRead]:
        events = self.session.query(EventModel).all()
        return [EventRead(**event.dict()) for event in events]
    
    def update(self, event_id: int, event: EventCreate) -> EventRead:
        event_model = self.session.query(EventModel).filter(EventModel.id == event_id).first()
        if event_model:
            event_model.name = event.name
            event_model.date = event.date
            self.session.commit()
            self.session.refresh(event_model)
            return EventRead(**event_model.dict())
        raise ValueError("Event not found")
    
    