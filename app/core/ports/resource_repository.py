from abc import ABC, abstractmethod
from app.core.domain.resource import Resource, ResourceCreate

class ResourceRepository(ABC):
    @abstractmethod
    def save(self, resource: ResourceCreate) -> Resource:
        pass

    @abstractmethod
    def find_by_id(self, resource_id: str) -> Resource:
        pass

    @abstractmethod
    def list_by_event(self, event_id: str) -> list[Resource]:
        pass