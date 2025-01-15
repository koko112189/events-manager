from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.domain.attendee import AttendeeCreate, AttendeeResponse
from app.core.services.attendee_service import AttendeeService
from app.infrastructure.database.postgres_attendee_repository import PostgresAttendeeRepository
from app.infrastructure.database.session import get_db

router = APIRouter()

@router.post("/attendees", response_model=AttendeeResponse, summary="Registrar un nuevo asistente", tags=["Asistentes"])
def register_attendee(attendee: AttendeeCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo asistente.

    Parámetros:
    - **attendee**: Un objeto `AttendeeCreate` con la información del asistente.

    Respuesta:
    - Un objeto `AttendeeResponse` con la información del asistente registrado.
    """
    try:
        repository = PostgresAttendeeRepository(db)
        service = AttendeeService(repository)
        new_attendee = service.register_attendee(attendee)
        return new_attendee
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/attendees/{attendee_id}", response_model=AttendeeResponse, summary="Obtener un asistente por ID", tags=["Asistentes"])
def get_attendee(attendee_id: str, db: Session = Depends(get_db)):
    """
    Obtiene un asistente por su ID.

    Parámetros:
    - **attendee_id**: El ID del asistente que se desea obtener.

    Respuesta:
    - Un objeto `AttendeeResponse` con la información del asistente.
    """
    try:
        repository = PostgresAttendeeRepository(db)
        service = AttendeeService(repository)
        attendee = service.get_attendee(attendee_id)
        return attendee
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/events/{event_id}/attendees", response_model=list[AttendeeResponse], summary="Listar asistentes de un evento", tags=["Asistentes"])
def list_attendees(event_id: str, db: Session = Depends(get_db)):
    """
    Lista todos los asistentes de un evento.

    Parámetros:
    - **event_id**: El ID del evento cuyos asistentes se desean listar.

    Respuesta:
    - Una lista de objetos `AttendeeResponse` con la información de los asistentes.
    """
    try:
        repository = PostgresAttendeeRepository(db)
        service = AttendeeService(repository)
        attendees = service.list_attendees(event_id)
        return attendees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))