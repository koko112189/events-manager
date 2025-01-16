import redis
from app.core.domain.events import Event
from app.config import settings

class EventCache:
    def __init__(self, client: redis.Redis):
        self.client = client

    def set_event(self, event: Event) -> None:
        self.client.set(f"event:{event.id}", event.json())

    def get_event(self, event_id: str) -> Event:
        event_data = self.client.get(f"event:{event_id}")
        if event_data:
            return Event.parse_raw(event_data)
        return None