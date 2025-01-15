from datetime import datetime
from app.core.domain.session import Session, SessionCreate
from app.core.ports.session_repository import SessionRepository

class SessionService:
    def __init__(self, session_repository: SessionRepository):
        self.session_repository = session_repository

    def create_session(self, session: SessionCreate) -> Session:
        if not self.session_repository.is_time_slot_available(session.event_id, session.start_time, session.end_time):
            raise ValueError("Time slot is not available")
        return self.session_repository.save(session)

    def get_session(self, session_id: str) -> Session:
        return self.session_repository.find_by_id(session_id)

    def list_sessions(self, event_id: str) -> list[Session]:
        return self.session_repository.list_by_event(event_id)

    def assign_speaker(self, session_id: str, speaker_id: str) -> Session:
        session = self.session_repository.find_by_id(session_id)
        session.speaker_id = speaker_id
        return self.session_repository.save(session)