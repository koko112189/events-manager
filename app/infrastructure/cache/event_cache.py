import json
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
        event_keys = self.client.keys("event:*")
        
        events = []
        for key in event_keys:
            event_data = self.client.get(key)  # Esto obtiene el valor (debería ser JSON)
            if event_data:
                try:
                    event_dict = json.loads(event_data)
                    event = EventRead.parse_obj(event_dict)  # Usa parse_obj para un diccionario
                    events.append(event)
                except json.JSONDecodeError as e:
                    print(f"Error decodificando JSON para la clave {key}: {e}")
        return events
    
    def set_events(self, events: list[EventRead]) -> None:
        for event in events:
            self.client.set(f"event:{event.id}", event.json())