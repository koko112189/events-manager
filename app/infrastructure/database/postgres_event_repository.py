from sqlalchemy.orm import Session
from app.core.ports.event_repository import EventRepository
from app.core.domain.event import Event
from app.infrastructure.database.models import EventModel  # Definiremos este modelo más adelante

class PostgresEventRepository(EventRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, event: Event) -> None:
        event_model = EventModel(**event.dict())
        self.session.add(event_model)
        self.session.commit()

    def find_by_id(self, event_id: str) -> Event:
        event_model = self.session.query(EventModel).filter(EventModel.id == event_id).first()
        if event_model:
            return Event(**event_model.dict())
        raise ValueError("Event not found")