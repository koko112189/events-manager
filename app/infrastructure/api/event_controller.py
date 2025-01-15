from fastapi import APIRouter, Depends, HTTPException
from app.core.services.event_service import EventService
from app.core.domain.event import Event
from app.infrastructure.database.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/events")
def create_event(event: Event, db: Session = Depends(get_db)):
    try:
        repository = PostgresEventRepository(db)
        service = EventService(repository)
        service.create_event(event)
        return {"message": "Event created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/events/{event_id}")
def get_event(event_id: str, db: Session = Depends(get_db)):
    try:
        repository = PostgresEventRepository(db)
        service = EventService(repository)
        event = service.get_event(event_id)
        return event
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))