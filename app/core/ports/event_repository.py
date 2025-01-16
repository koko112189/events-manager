from abc import ABC, abstractmethod
from app.core.domain.events import Event

class EventRepository(ABC):
    @abstractmethod
    def save(self, event: Event) -> None:
        pass

    @abstractmethod
    def find_by_id(self, event_id: str) -> Event:
        pass