from datetime import datetime, timezone
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
        if self.is_future_date(event.date):
            raise ValueError("Event date is in the past")
        created_event = self.event_repository.save(event)
        self.event_cache.set_event(created_event)
        print ("Event created")

    def get_event(self, event_id: str) -> EventRead:
        return self.event_repository.find_by_id(event_id)
    
    def list_events(self) -> list[EventRead]:
        cached_events = self.event_cache.get_events()
        if cached_events:
            print("Using cache")
            return cached_events
        
        return self.event_repository.list_events()
    
    def update_event(self, event_id: int, event: EventCreate) -> EventRead:
        updated_event = self.event_repository.update(event_id, event)
        #self.event_cache.set_event(updated_event)
        print ("Event updated")

    def is_future_date(self,event_date: datetime) -> bool:
        current_date = datetime.now(timezone.utc)
        if event_date.tzinfo is None:
            event_date = event_date.replace(tzinfo=timezone.utc)
        return event_date > current_date