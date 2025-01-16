import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.config import settings

class EmailService:
    def __init__(self):
        self.sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

    def send_email(self, to_email: str, subject: str, content: str):
        message = Mail(
            from_email=settings.EMAIL_FROM,
            to_emails=to_email,
            subject=subject,
            html_content=content
        )
        try:
            response = self.sg.send(message)
            return response.status_code
        except Exception as e:
            print(f"Error sending email: {e}")
            return None