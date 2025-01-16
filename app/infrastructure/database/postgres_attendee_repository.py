from typing import Type
from annotated_types import T
from sqlalchemy.orm import Session
from app.core.domain.attendee import AttendeeCreate, AttendeeRead
from app.core.ports.attendee_repository import AttendeeRepository
from app.infrastructure.database.models import Attendee as AttendeeModel

class PostgresAttendeeRepository(AttendeeRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, attendee: AttendeeCreate) -> AttendeeCreate:
        new_attendee = AttendeeModel(**attendee.dict())
        self.session.add(attendee)
        self.session.commit()
        self.session.refresh(attendee)
        return new_attendee

    def find_by_id(self, attendee_id: int) -> AttendeeRead:
        attendee_model = self.session.query(AttendeeModel).filter(AttendeeModel.id == attendee_id).first()
        if attendee_model:
            return AttendeeRead.from_orm(attendee_model)
        raise ValueError("Attendee not found")

    def list_by_event(self, event_id: int) -> list[AttendeeRead]:
        attendees = self.session.query(AttendeeModel).filter(AttendeeModel.event_id == event_id).all()
        return [AttendeeRead.from_orm(attendee) for attendee in attendees]