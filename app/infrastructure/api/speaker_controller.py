from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.domain.speaker import  SpeakerCreate, SpeakerRead
from app.core.services.speaker_service import SpeakerService
from app.infrastructure.database.postgres_speaker_repository import PostgresSpeakerRepository
from app.infrastructure.database.session import get_db

router = APIRouter()

@router.post("/speakers", response_model=SpeakerCreate, summary="Crear un nuevo ponente", tags=["Ponentes"])
def create_speaker(speaker: SpeakerCreate, db: Session = Depends(get_db)):
    try:
        repository = PostgresSpeakerRepository(db)
        service = SpeakerService(repository)
        new_speaker = service.create_speaker(speaker)
        return new_speaker
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/speakers/{speaker_id}", response_model=SpeakerRead, summary="Obtener un ponente por ID", tags=["Ponentes"])
def get_speaker(speaker_id: str, db: Session = Depends(get_db)):
    try:
        repository = PostgresSpeakerRepository(db)
        service = SpeakerService(repository)
        speaker = service.get_speaker(speaker_id)
        return speaker
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/events/{event_id}/speakers", response_model=list[SpeakerRead], summary="Listar ponentes de un evento", tags=["Ponentes"])
def list_speakers(event_id: str, db: Session = Depends(get_db)):
    try:
        repository = PostgresSpeakerRepository(db)
        service = SpeakerService(repository)
        speakers = service.list_speakers(event_id)
        return speakers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))