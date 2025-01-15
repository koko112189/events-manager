from abc import ABC, abstractmethod
from app.core.domain.attendee import Attendee, AttendeeCreate

class AttendeeRepository(ABC):
    @abstractmethod
    def save(self, attendee: AttendeeCreate) -> Attendee:
        pass

    @abstractmethod
    def find_by_id(self, attendee_id: str) -> Attendee:
        pass

    @abstractmethod
    def list_by_event(self, event_id: str) -> list[Attendee]:
        pass