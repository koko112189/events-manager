import pytest
from app.core.services.resource_service import ResourceService
from app.core.ports.resource_repository import ResourceRepository
from app.core.domain.resource import Resource, ResourceCreate

class MockResourceRepository(ResourceRepository):
    def save(self, resource: ResourceCreate) -> Resource:
        return Resource(id="1", **resource.dict())

    def find_by_id(self, resource_id: str) -> Resource:
        return Resource(id=resource_id, name="Test Resource", description="Test", event_id="1")

    def list_by_event(self, event_id: str) -> list[Resource]:
        return [Resource(id="1", name="Test Resource", description="Test", event_id=event_id)]

def test_add_resource():
    repo = MockResourceRepository()
    service = ResourceService(repo)
    resource = service.add_resource(ResourceCreate(name="Test Resource", description="Test", event_id="1"))
    assert resource.name == "Test Resource"

def test_list_resources():
    repo = MockResourceRepository()
    service = ResourceService(repo)
    resources = service.list_resources("1")
    assert len(resources) == 1