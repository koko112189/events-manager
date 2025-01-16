from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.domain.session import  SessionCreate, SessionRead
from app.core.services.session_service import SessionService
from app.infrastructure.database.postgres_session_repository import PostgresSessionRepository
from app.infrastructure.database.session import get_db

router = APIRouter()

@router.post("/sessions", response_model=SessionCreate, summary="Crear una nueva sesión", tags=["Sesiones"])
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
    try:
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        new_session = service.create_session(session)
        return new_session
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/sessions/{session_id}", response_model=SessionRead, summary="Obtener una sesión por ID", tags=["Sesiones"])
def get_session(session_id: str, db: Session = Depends(get_db)):
    try:
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        session = service.get_session(session_id)
        return session
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/events/{event_id}/sessions", response_model=list[SessionRead], summary="Listar sesiones de un evento", tags=["Sesiones"])
def list_sessions(event_id: str, db: Session = Depends(get_db)):
    try:
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        sessions = service.list_sessions(event_id)
        return sessions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/sessions/{session_id}/assign-speaker", response_model=SessionRead, summary="Asignar un ponente a una sesión", tags=["Sesiones"])
def assign_speaker(session_id: str, speaker_id: str, db: Session = Depends(get_db)):
    try:
        repository = PostgresSessionRepository(db)
        service = SessionService(repository)
        session = service.assign_speaker(session_id, speaker_id)
        return session
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))