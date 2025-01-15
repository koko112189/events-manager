from app.core.ports.event_repository import EventRepository
from app.core.domain.event import Event

class EventService:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def create_event(self, event: Event) -> None:
        self.event_repository.save(event)

    def get_event(self, event_id: str) -> Event:
        return self.event_repository.find_by_id(event_id)