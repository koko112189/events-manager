from app.core.ports.event_repository import EventRepository
from app.core.domain.events import EventCreate, EventRead
from app.core.tasks.redis import get_redis
from app.infrastructure.cache.event_cache import EventCache

class EventService:
    def __init__(self, event_repository: EventRepository):
        self.redis = get_redis()
        self.event_repository = event_repository
        self.event_cache = EventCache(self.redis)

    def create_event(self, event: EventCreate) -> None:
        self.event_repository.save(event)

    def get_event(self, event_id: str) -> EventRead:
        return self.event_repository.find_by_id(event_id)
    
    def list_events(self) -> list[EventRead]:
        cached_events = self.event_cache.get_events()
        if cached_events:
            return cached_events
        
        return self.event_repository.list_events()