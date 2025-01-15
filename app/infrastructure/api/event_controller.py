from app.infrastructure.database.postgres_event_repository import PostgresEventRepository
from fastapi import APIRouter, Depends, HTTPException
from app.core.services.event_service import EventService
from app.core.domain.event import Event
from app.infrastructure.database.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post(
    "/events",
    response_model=dict,
    summary="Crear un nuevo evento",
    description="Crea un nuevo evento con la información proporcionada.",
    tags=["Eventos"]
)
def create_event(event: Event, db: Session = Depends(get_db)):
    """
    Crea un nuevo evento.

    Parámetros:
    - **event**: Un objeto `Event` con la información del evento.

    Respuesta:
    - Un mensaje de éxito si el evento se crea correctamente.
    """
    try:
        repository = PostgresEventRepository(db)
        service = EventService(repository)
        service.create_event(event)
        return {"message": "Event created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/events/{event_id}",
    response_model=Event,
    summary="Obtener un evento por ID",
    description="Obtiene la información de un evento específico utilizando su ID.",
    tags=["Eventos"]
)
def get_event(event_id: str, db: Session = Depends(get_db)):
    """
    Obtiene un evento por su ID.

    Parámetros:
    - **event_id**: El ID del evento que se desea obtener.

    Respuesta:
    - Un objeto `Event` con la información del evento.
    """
    try:
        repository = PostgresEventRepository(db)
        service = EventService(repository)
        event = service.get_event(event_id)
        return event
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))