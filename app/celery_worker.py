from datetime import timedelta
from celery import Celery
from app.config import settings

celery = Celery(__name__, broker=settings.REDIS_URL, backend=settings.REDIS_URL)

celery.conf.update(
    result_expires=3600,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery.conf.beat_schedule = {
    "send-event-reminders": {
        "task": "app.core.tasks.email_tasks.send_reminder_email",
        "schedule": timedelta(days=1),  
    },
}