from abc import ABC, abstractmethod
from app.core.domain.resource import ResourceCreate, ResourceRead

class ResourceRepository(ABC):
    @abstractmethod
    def save(self, resource: ResourceCreate) -> ResourceCreate:
        pass

    @abstractmethod
    def find_by_id(self, resource_id: int) -> ResourceRead:
        pass

    @abstractmethod
    def list_by_event(self, event_id: int) -> list[ResourceRead]:
        pass