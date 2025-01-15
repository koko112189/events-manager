import pytest
from app.core.services.attendee_service import AttendeeService
from app.core.ports.attendee_repository import AttendeeRepository
from app.core.domain.attendee import Attendee, AttendeeCreate

class MockAttendeeRepository(AttendeeRepository):
    def save(self, attendee: AttendeeCreate) -> Attendee:
        return Attendee(id="1", **attendee.dict())

    def find_by_id(self, attendee_id: str) -> Attendee:
        return Attendee(id=attendee_id, name="Test Attendee", email="test@example.com", event_id="1")

    def list_by_event(self, event_id: str) -> list[Attendee]:
        return [Attendee(id="1", name="Test Attendee", email="test@example.com", event_id=event_id)]

def test_register_attendee():
    repo = MockAttendeeRepository()
    service = AttendeeService(repo)
    attendee = service.register_attendee(AttendeeCreate(name="Test Attendee", email="test@example.com", event_id="1"))
    assert attendee.name == "Test Attendee"

def test_get_attendee():
    repo = MockAttendeeRepository()
    service = AttendeeService(repo)
    attendee = service.get_attendee("1")
    assert attendee.id == "1"

def test_list_attendees():
    repo = MockAttendeeRepository()
    service = AttendeeService(repo)
    attendees = service.list_attendees("1")
    assert len(attendees) == 1