from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.config.settings import settings

class EmailService:
    def __init__(self):
        self.smtp_server = settings.SMTP_SERVER
        self.smtp_port = settings.SMTP_PORT
        self.username = settings.SMTP_USERNAME
        self.password = settings.SMTP_PASSWORD

    def send_email(self, to_email: str, subject: str, content: str):
        message = MIMEMultipart()
        message["From"] = self.username
        message["To"] = to_email
        message["Subject"] = subject

        message.attach(MIMEText(content, "plain"))
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.username, to_email, content.as_string())
        except Exception as e:
            print(f"Error sending email: {e}")
            return None