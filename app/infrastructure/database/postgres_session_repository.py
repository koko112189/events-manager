from datetime import datetime
from sqlalchemy.orm import Session
from app.core.domain.session import Session, SessionCreate
from app.core.ports.session_repository import SessionRepository
from app.infrastructure.database.models import SessionModel

class PostgresSessionRepository(SessionRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, session: SessionCreate) -> Session:
        session_model = SessionModel(**session.dict())
        self.session.add(session_model)
        self.session.commit()
        self.session.refresh(session_model)
        return Session.from_orm(session_model)

    def find_by_id(self, session_id: str) -> Session:
        session_model = self.session.query(SessionModel).filter(SessionModel.id == session_id).first()
        if session_model:
            return Session.from_orm(session_model)
        raise ValueError("Session not found")

    def list_by_event(self, event_id: str) -> list[Session]:
        sessions = self.session.query(SessionModel).filter(SessionModel.event_id == event_id).all()
        return [Session.from_orm(session) for session in sessions]

    def is_time_slot_available(self, event_id: str, start_time: datetime, end_time: datetime) -> bool:
        conflicting_sessions = self.session.query(SessionModel).filter(
            SessionModel.event_id == event_id,
            SessionModel.start_time < end_time,
            SessionModel.end_time > start_time
        ).count()
        return conflicting_sessions == 0