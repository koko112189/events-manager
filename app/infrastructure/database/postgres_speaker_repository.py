from sqlalchemy.orm import Session
from app.core.domain.speaker import Speaker, SpeakerCreate
from app.core.ports.speaker_repository import SpeakerRepository
from app.infrastructure.database.models import SpeakerModel

class PostgresSpeakerRepository(SpeakerRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, speaker: SpeakerCreate) -> Speaker:
        speaker_model = SpeakerModel(**speaker.dict())
        self.session.add(speaker_model)
        self.session.commit()
        self.session.refresh(speaker_model)
        return Speaker.from_orm(speaker_model)

    def find_by_id(self, speaker_id: str) -> Speaker:
        speaker_model = self.session.query(SpeakerModel).filter(SpeakerModel.id == speaker_id).first()
        if speaker_model:
            return Speaker.from_orm(speaker_model)
        raise ValueError("Speaker not found")

    def list_by_event(self, event_id: str) -> list[Speaker]:
        speakers = self.session.query(SpeakerModel).filter(SpeakerModel.event_id == event_id).all()
        return [Speaker.from_orm(speaker) for speaker in speakers]