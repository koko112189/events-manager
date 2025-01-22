from abc import ABC, abstractmethod
from datetime import datetime
from app.core.domain.session import SessionCreate, SessionRead

class SessionRepository(ABC):
    @abstractmethod
    def save(self, session: SessionCreate) -> SessionCreate:
        pass

    @abstractmethod
    def find_by_id(self, session_id: int) -> SessionRead:
        pass

    @abstractmethod
    def list_by_event(self, event_id: int) -> list[SessionRead]:
        pass

    @abstractmethod
    def count_attendees(self, session_id: int) -> int:
        pass

    @abstractmethod
    def is_time_slot_available(self, event_id: int, start_time: datetime, end_time: datetime) -> bool:
        pass