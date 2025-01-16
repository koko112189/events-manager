from celery import shared_task
from app.core.services.email_service import EmailService

email_service = EmailService()

@shared_task
def send_confirmation_email(to_email: str, event_name: str):
    subject = f"Confirmación de Registro - {event_name}"
    content = f"Gracias por registrarte en el evento {event_name}."
    email_service.send_email(to_email, subject, content)

@shared_task
def send_reminder_email(to_email: str, event_name: str, event_date: str):
    subject = f"Recordatorio - {event_name}"
    content = f"Te recordamos que el evento {event_name} es el {event_date}."
    email_service.send_email(to_email, subject, content)

@shared_task
def send_change_notification(to_email: str, event_name: str, changes: str):
    subject = f"Cambios en el Evento - {event_name}"
    content = f"Se han realizado cambios en el evento {event_name}: {changes}."
    email_service.send_email(to_email, subject, content)

@shared_task
def send_capacity_notification(to_email: str, session_name: str):
    subject = f"Capacidad Alcanzada - {session_name}"
    content = f"La sesión {session_name} ha alcanzado el 90% de su capacidad."
    email_service.send_email(to_email, subject, content)