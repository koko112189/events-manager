import pytest
from datetime import datetime
from app.core.services.session_service import SessionService
from app.core.ports.session_repository import SessionRepository
from app.core.domain.session import Session, SessionCreate

class MockSessionRepository(SessionRepository):
    def save(self, session: SessionCreate) -> Session:
        return Session(id="1", **session.dict())

    def find_by_id(self, session_id: str) -> Session:
        return Session(id=session_id, name="Test Session", description="Test", start_time=datetime.now(), end_time=datetime.now(), event_id="1")

    def list_by_event(self, event_id: str) -> list[Session]:
        return [Session(id="1", name="Test Session", description="Test", start_time=datetime.now(), end_time=datetime.now(), event_id=event_id)]

    def is_time_slot_available(self, event_id: str, start_time: datetime, end_time: datetime) -> bool:
        return True

def test_create_session():
    repo = MockSessionRepository()
    service = SessionService(repo)
    session = service.create_session(SessionCreate(name="Test Session", description="Test", start_time=datetime.now(), end_time=datetime.now(), event_id="1"))
    assert session.name == "Test Session"

def test_get_session():
    repo = MockSessionRepository()
    service = SessionService(repo)
    session = service.get_session("1")
    assert session.id == "1"

def test_list_sessions():
    repo = MockSessionRepository()
    service = SessionService(repo)
    sessions = service.list_sessions("1")
    assert len(sessions) == 1