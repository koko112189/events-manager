from sqlalchemy.orm import Session
from app.core.domain.attendee import Attendee, AttendeeCreate
from app.core.ports.attendee_repository import AttendeeRepository
from app.infrastructure.database.models import AttendeeModel

class PostgresAttendeeRepository(AttendeeRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, attendee: AttendeeCreate) -> Attendee:
        attendee_model = AttendeeModel(**attendee.dict())
        self.session.add(attendee_model)
        self.session.commit()
        self.session.refresh(attendee_model)
        return Attendee.from_orm(attendee_model)

    def find_by_id(self, attendee_id: str) -> Attendee:
        attendee_model = self.session.query(AttendeeModel).filter(AttendeeModel.id == attendee_id).first()
        if attendee_model:
            return Attendee.from_orm(attendee_model)
        raise ValueError("Attendee not found")

    def list_by_event(self, event_id: str) -> list[Attendee]:
        attendees = self.session.query(AttendeeModel).filter(AttendeeModel.event_id == event_id).all()
        return [Attendee.from_orm(attendee) for attendee in attendees]