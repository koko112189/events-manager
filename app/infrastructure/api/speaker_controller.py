from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.domain.speaker import SpeakerCreate, SpeakerRead
from app.core.services.speaker_service import SpeakerService
from app.infrastructure.database.postgres_speaker_repository import PostgresSpeakerRepository
from app.infrastructure.database.session import get_db

# Definición del router
router = APIRouter()

@router.post(
    "/speakers",
    response_model=SpeakerCreate,
    summary="Crear un nuevo ponente",
    description="Crea un nuevo ponente con la información proporcionada.",
    tags=["Ponentes"],
    responses={
        200: {
            "description": "Ponente creado correctamente",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "person_id": 1,
                        "bio": "Experto en Python y FastAPI."
                    }
                }
            },
        },
        400: {
            "description": "Error en la solicitud",
            "content": {
                "application/json": {
                    "example": {"detail": "La información proporcionada no es válida."}
                }
            },
        },
    },
)
def create_speaker(speaker: SpeakerCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo ponente.

    Parámetros:
    - **speaker**: Un objeto `SpeakerCreate` con la información del ponente.

    Respuesta:
    - Un objeto `SpeakerCreate` con la información del ponente creado.

    Errores:
    - **400**: Si la información proporcionada no es válida.
    """
    try:
        repository = PostgresSpeakerRepository(db)
        service = SpeakerService(repository)
        new_speaker = service.create_speaker(speaker)
        return new_speaker
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/speakers/{speaker_id}",
    response_model=SpeakerRead,
    summary="Obtener un ponente por ID",
    description="Obtiene la información de un ponente específico utilizando su ID.",
    tags=["Ponentes"],
    responses={
        200: {
            "description": "Ponente encontrado",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "person_id": 1,
                        "bio": "Experto en Python y FastAPI."
                    }
                }
            },
        },
        404: {
            "description": "Ponente no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "El ponente con ID 1 no existe."}
                }
            },
        },
    },
)
def get_speaker(speaker_id: str, db: Session = Depends(get_db)):
    """
    Obtiene un ponente por su ID.

    Parámetros:
    - **speaker_id**: El ID del ponente que se desea obtener.

    Respuesta:
    - Un objeto `SpeakerRead` con la información del ponente.

    Errores:
    - **404**: Si el ponente no existe.
    """
    try:
        repository = PostgresSpeakerRepository(db)
        service = SpeakerService(repository)
        speaker = service.get_speaker(speaker_id)
        return speaker
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get(
    "/events/{event_id}/speakers",
    response_model=list[SpeakerRead],
    summary="Listar ponentes de un evento",
    description="Lista todos los ponentes asociados a un evento específico.",
    tags=["Ponentes"],
    responses={
        200: {
            "description": "Lista de ponentes",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1,
                            "person_id": 1,
                            "bio": "Experto en Python y FastAPI."
                        },
                        {
                            "id": 2,
                            "person_id": 2,
                            "bio": "Especialista en bases de datos."
                        },
                    ]
                }
            },
        },
        500: {
            "description": "Error interno del servidor",
            "content": {
                "application/json": {
                    "example": {"detail": "Ocurrió un error al listar los ponentes."}
                }
            },
        },
    },
)
def list_speakers(event_id: str, db: Session = Depends(get_db)):
    """
    Lista todos los ponentes asociados a un evento específico.

    Parámetros:
    - **event_id**: El ID del evento cuyos ponentes se desean listar.

    Respuesta:
    - Una lista de objetos `SpeakerRead` con la información de los ponentes.

    Errores:
    - **500**: Si ocurre un error interno al listar los ponentes.
    """
    try:
        repository = PostgresSpeakerRepository(db)
        service = SpeakerService(repository)
        speakers = service.list_speakers(event_id)
        return speakers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))