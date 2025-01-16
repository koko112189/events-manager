from app.core.ports.event_repository import EventRepository
from app.core.domain.events import Event
from app.infrastructure.cache.event_cache import EventCache

class EventService:
    def __init__(self, event_repository: EventRepository, event_cache: EventCache):
        self.event_repository = event_repository
        self.event_cache = event_cache

    def create_event(self, event: Event) -> None:
        self.event_repository.save(event)

    def get_event(self, event_id: str) -> Event:
        return self.event_repository.find_by_id(event_id)