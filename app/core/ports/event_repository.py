from abc import ABC, abstractmethod
from app.core.domain.events import  EventCreate, EventRead

class EventRepository(ABC):
    @abstractmethod
    def save(self, event: EventCreate) -> None:
        pass

    @abstractmethod
    def find_by_id(self, event_id: int) -> EventRead:
        pass

    @abstractmethod
    def list_events(self) -> list[EventRead]:
        pass