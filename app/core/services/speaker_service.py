from app.core.domain.speaker import Speaker, SpeakerCreate
from app.core.ports.speaker_repository import SpeakerRepository

class SpeakerService:
    def __init__(self, speaker_repository: SpeakerRepository):
        self.speaker_repository = speaker_repository

    def create_speaker(self, speaker: SpeakerCreate) -> Speaker:
        return self.speaker_repository.save(speaker)

    def get_speaker(self, speaker_id: str) -> Speaker:
        return self.speaker_repository.find_by_id(speaker_id)

    def list_speakers(self, event_id: str) -> list[Speaker]:
        return self.speaker_repository.list_by_event(event_id)