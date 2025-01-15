from app.core.domain.attendee import Attendee, AttendeeCreate
from app.core.ports.attendee_repository import AttendeeRepository

class AttendeeService:
    def __init__(self, attendee_repository: AttendeeRepository):
        self.attendee_repository = attendee_repository

    def register_attendee(self, attendee: AttendeeCreate) -> Attendee:
        return self.attendee_repository.save(attendee)

    def get_attendee(self, attendee_id: str) -> Attendee:
        return self.attendee_repository.find_by_id(attendee_id)

    def list_attendees(self, event_id: str) -> list[Attendee]:
        return self.attendee_repository.list_by_event(event_id)