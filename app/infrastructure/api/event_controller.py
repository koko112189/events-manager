from app.infrastructure.cache import event_cache
from app.infrastructure.database.postgres_event_repository import PostgresEventRepository
from fastapi import APIRouter, Depends, HTTPException
from app.core.services.event_service import EventService
from app.core.domain.events import  EventCreate, EventRead
from app.infrastructure.database.session import get_db
from sqlalchemy.orm import Session
from app.core.tasks.email_tasks import send_change_notification

router = APIRouter()

@router.post(
    "/events",
    response_model=dict,
    summary="Crear un nuevo evento",
    description="Crea un nuevo evento con la información proporcionada.",
    tags=["Eventos"]
)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
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
    response_model=EventRead,
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
    
@router.get("/events", response_model=list[EventRead], summary="Listar todos los eventos", tags=["Eventos"])
def list_events(db: Session = Depends(get_db)):
    """
    Lista todos los eventos.

    Respuesta:
    - Una lista de objetos `EventResponse` con la información de los eventos.
    """
    try:
        # cached_events = event_cache.get_events()
        # if cached_events:
        #     return cached_events
        
        repository = PostgresEventRepository(db)
        service = EventService(repository)
        events = service.list_events()
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/events/{event_id}", response_model=EventRead, summary="Actualizar un evento", tags=["Eventos"])
def update_event(event_id: str, event: EventCreate, db: Session = Depends(get_db)):
    """
    Actualiza un evento existente.

    Parámetros:
    - **event_id**: El ID del evento que se desea actualizar.
    - **event**: Un objeto `EventCreate` con la información actualizada del evento.

    Respuesta:
    - Un objeto `EventResponse` con la información del evento actualizado.
    """
    try:
        repository = PostgresEventRepository(db)
        service = EventService(repository)
        updated_event = service.update_event(event_id, event)

        changes = f"Nuevo nombre: {updated_event.name}, Nueva fecha: {updated_event.date}"
        send_change_notification.delay(updated_event.attendees[0].email, updated_event.name, changes)

        return updated_event
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/events/{event_id}", summary="Eliminar un evento", tags=["Eventos"])
def delete_event(event_id: str, db: Session = Depends(get_db)):
    """
    Elimina un evento por su ID.

    Parámetros:
    - **event_id**: El ID del evento que se desea eliminar.

    Respuesta:
    - Un mensaje de éxito si el evento se elimina correctamente.
    """
    try:
        repository = PostgresEventRepository(db)
        service = EventService(repository)
        service.delete_event(event_id)
        return {"message": "Event deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))