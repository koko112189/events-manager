from app.core.domain.attendee import AttendeeRead, AttendeeCreate
from app.core.ports.attendee_repository import AttendeeRepository
from app.core.ports.session_repository import SessionRepository
from app.core.tasks.email_tasks import send_capacity_notification, send_confirmation_email

class AttendeeService:
    def __init__(self, attendee_repository: AttendeeRepository, session_repository: SessionRepository):
        self.attendee_repository = attendee_repository
        self.session_repository = session_repository

    def register_attendee(self, attendee: AttendeeCreate) -> None:
        count_attendees = self.session_repository.count_attendees(attendee.session_id)
        session = self.session_repository.find_by_id(attendee.session_id)
        if count_attendees >= session.capacity:
            raise ValueError("Session is full")
        if session.capacity * 0.9 <= count_attendees:
            print("Send capacity 90% notification")
        new_attendee =  self.attendee_repository.save(attendee)
        send_confirmation_email(new_attendee.email, new_attendee.event.name)
        return new_attendee

    def get_attendee(self, attendee_id: str) -> AttendeeRead:
        return self.attendee_repository.find_by_id(attendee_id)

    def list_attendees(self, event_id: str) -> list[AttendeeRead]:
        return self.attendee_repository.list_by_event(event_id)