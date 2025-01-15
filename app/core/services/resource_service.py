from app.core.domain.resource import Resource, ResourceCreate
from app.core.ports.resource_repository import ResourceRepository

class ResourceService:
    def __init__(self, resource_repository: ResourceRepository):
        self.resource_repository = resource_repository

    def add_resource(self, resource: ResourceCreate) -> Resource:
        return self.resource_repository.save(resource)

    def get_resource(self, resource_id: str) -> Resource:
        return self.resource_repository.find_by_id(resource_id)

    def list_resources(self, event_id: str) -> list[Resource]:
        return self.resource_repository.list_by_event(event_id)