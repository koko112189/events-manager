from abc import ABC, abstractmethod
from app.core.domain.attendee import AttendeeCreate, AttendeeRead

class AttendeeRepository(ABC):
    @abstractmethod
    def save(self, attendee: AttendeeCreate) -> None:
        pass

    @abstractmethod
    def find_by_id(self, attendee_id: int) -> AttendeeRead:
        pass

    @abstractmethod
    def list_by_event(self, event_id: int) -> list[AttendeeRead]:
        pass