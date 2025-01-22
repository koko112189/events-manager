from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.domain.session import SessionCreate, SessionRead
from app.core.services.session_service import SessionService
from app.infrastructure.database.postgres_session_repository import PostgresSessionRepository
from app.infrastructure.database.session import get_db
import logging

# Configuración del logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Definición del router
router = APIRouter()

@router.post(
    "/sessions",
    summary="Crear una nueva sesión",
    description="Crea una nueva sesión con la información proporcionada.",
    tags=["Sesiones"],
    responses={
        200: {
            "description": "Sesión creada correctamente",
            "content": {
                "application/json": {
                    "example": {"message": "Session created successfully"}
                }
            },
        },
        400: {
            "description": "Error en la solicitud",
            "content": {
                "application/json": {
                    "example": {"detail": "La fecha de la sesión no es válida."}
                }
            },
        },
    },
)
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva sesión.

    Parámetros:
    - **session**: Un objeto `SessionCreate` con la información de la sesión.

    Respuesta:
    - Un mensaje de éxito si la sesión se crea correctamente.

    Errores:
    - **400**: Si la información proporcionada no es válida.
    """
    try:
        logger.debug("Creating session: %s", session)
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        service.create_session(session)
        return {"message": "Session created successfully"}
    except ValueError as e:
        logger.error("Error creating session: %s", str(e))
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/sessions/{session_id}",
    response_model=SessionRead,
    summary="Obtener una sesión por ID",
    description="Obtiene la información de una sesión específica utilizando su ID.",
    tags=["Sesiones"],
    responses={
        200: {
            "description": "Sesión encontrada",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Sesión de Python",
                        "capacity": 50,
                        "start_time": "2023-10-15T10:00:00",
                        "end_time": "2023-10-15T12:00:00",
                        "date": "2023-10-15",
                        "event_id": 1,
                        "speaker_id": 1,
                    }
                }
            },
        },
        404: {
            "description": "Sesión no encontrada",
            "content": {
                "application/json": {
                    "example": {"detail": "La sesión con ID 1 no existe."}
                }
            },
        },
    },
)
def get_session(session_id: str, db: Session = Depends(get_db)):
    """
    Obtiene una sesión por su ID.

    Parámetros:
    - **session_id**: El ID de la sesión que se desea obtener.

    Respuesta:
    - Un objeto `SessionRead` con la información de la sesión.

    Errores:
    - **404**: Si la sesión no existe.
    """
    try:
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        session = service.get_session(session_id)
        return session
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get(
    "/events/{event_id}/sessions",
    response_model=list[SessionRead],
    summary="Listar sesiones de un evento",
    description="Lista todas las sesiones asociadas a un evento específico.",
    tags=["Sesiones"],
    responses={
        200: {
            "description": "Lista de sesiones",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "name": "Sesión de Python",
                            "capacity": 50,
                            "start_time": "2023-10-15T10:00:00",
                            "end_time": "2023-10-15T12:00:00",
                            "date": "2023-10-15",
                            "event_id": 1,
                            "speaker_id": 1,
                        },
                        {
                            "id": 2,
                            "name": "Sesión de FastAPI",
                            "capacity": 30,
                            "start_time": "2023-10-15T14:00:00",
                            "end_time": "2023-10-15T16:00:00",
                            "date": "2023-10-15",
                            "event_id": 1,
                            "speaker_id": 2,
                        },
                    ]
                }
            },
        },
        500: {
            "description": "Error interno del servidor",
            "content": {
                "application/json": {
                    "example": {"detail": "Ocurrió un error al listar las sesiones."}
                }
            },
        },
    },
)
def list_sessions(event_id: str, db: Session = Depends(get_db)):
    """
    Lista todas las sesiones asociadas a un evento específico.

    Parámetros:
    - **event_id**: El ID del evento cuyas sesiones se desean listar.

    Respuesta:
    - Una lista de objetos `SessionRead` con la información de las sesiones.

    Errores:
    - **500**: Si ocurre un error interno al listar las sesiones.
    """
    try:
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        sessions = service.list_sessions(event_id)
        return sessions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/sessions/{session_id}/assign-speaker",
    response_model=SessionRead,
    summary="Asignar un ponente a una sesión",
    description="Asigna un ponente a una sesión específica utilizando el ID de la sesión y el ID del ponente.",
    tags=["Sesiones"],
    responses={
        200: {
            "description": "Ponente asignado correctamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "name": "Sesión de Python",
                        "capacity": 50,
                        "start_time": "2023-10-15T10:00:00",
                        "end_time": "2023-10-15T12:00:00",
                        "date": "2023-10-15",
                        "event_id": 1,
                        "speaker_id": 1,
                    }
                }
            },
        },
        400: {
            "description": "Error en la solicitud",
            "content": {
                "application/json": {
                    "example": {"detail": "El ID del ponente no es válido."}
                }
            },
        },
        404: {
            "description": "Sesión no encontrada",
            "content": {
                "application/json": {
                    "example": {"detail": "La sesión con ID 1 no existe."}
                }
            },
        },
    },
)
def assign_speaker(session_id: str, speaker_id: str, db: Session = Depends(get_db)):
    """
    Asigna un ponente a una sesión específica.

    Parámetros:
    - **session_id**: El ID de la sesión a la que se desea asignar el ponente.
    - **speaker_id**: El ID del ponente que se desea asignar a la sesión.

    Respuesta:
    - Un objeto `SessionRead` con la información actualizada de la sesión.

    Errores:
    - **400**: Si el ID del ponente no es válido o no se puede asignar.
    - **404**: Si la sesión no existe.
    """
    try:
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        session = service.assign_speaker(session_id, speaker_id)
        return session
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))