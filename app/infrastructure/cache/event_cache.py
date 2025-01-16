import redis
from app.core.domain.events import  EventCreate, EventRead
from app.config import settings

class EventCache:
    def __init__(self, client: redis.Redis):
        self.client = client

    def set_event(self, event: EventCreate) -> None:
        self.client.set(f"event:{event.id}", event.json())

    def get_event(self, event_id: str) -> EventRead:
        event_data = self.client.get(f"event:{event_id}")
        if event_data:
            return EventRead.parse_raw(event_data)
        return None
    
    def get_events(self) -> list[EventRead]:
        events_data = self.client.keys("event:*")
        return [EventRead.parse_raw(event_data) for event_data in events_data]
    
    def set_events(self, events: list[EventRead]) -> None:
        for event in events:
            self.client.set(f"event:{event.id}", event.json())