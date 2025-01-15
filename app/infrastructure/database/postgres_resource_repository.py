from sqlalchemy.orm import Session
from app.core.domain.resource import Resource, ResourceCreate
from app.core.ports.resource_repository import ResourceRepository
from app.infrastructure.database.models import ResourceModel

class PostgresResourceRepository(ResourceRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, resource: ResourceCreate) -> Resource:
        resource_model = ResourceModel(**resource.dict())
        self.session.add(resource_model)
        self.session.commit()
        self.session.refresh(resource_model)
        return Resource.from_orm(resource_model)

    def find_by_id(self, resource_id: str) -> Resource:
        resource_model = self.session.query(ResourceModel).filter(ResourceModel.id == resource_id).first()
        if resource_model:
            return Resource.from_orm(resource_model)
        raise ValueError("Resource not found")

    def list_by_event(self, event_id: str) -> list[Resource]:
        resources = self.session.query(ResourceModel).filter(ResourceModel.event_id == event_id).all()
        return [Resource.from_orm(resource) for resource in resources]