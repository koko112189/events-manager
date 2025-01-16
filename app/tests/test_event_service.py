import pytest
from app.core.services.event_service import EventService
from app.core.ports.event_repository import EventRepository
from app.core.domain.events import Event
from datetime import datetime

class MockEventRepository(EventRepository):
    def save(self, event: Event) -> None:
        pass

    def find_by_id(self, event_id: str) -> Event:
        return Event(id=event_id, name="Test Event", description="Test", date=datetime.now(), location="Test Location")

def test_get_event():
    repo = MockEventRepository()
    service = EventService(repo, None, None)
    event = service.get_event("1")
    assert event.name == "Test Event"