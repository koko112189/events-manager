from abc import ABC, abstractmethod
from datetime import datetime
from app.core.domain.session import Session, SessionCreate

class SessionRepository(ABC):
    @abstractmethod
    def save(self, session: SessionCreate) -> Session:
        pass

    @abstractmethod
    def find_by_id(self, session_id: str) -> Session:
        pass

    @abstractmethod
    def list_by_event(self, event_id: str) -> list[Session]:
        pass

    @abstractmethod
    def is_time_slot_available(self, event_id: str, start_time: datetime, end_time: datetime) -> bool:
        pass