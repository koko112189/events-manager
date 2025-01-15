from abc import ABC, abstractmethod
from app.core.domain.speaker import Speaker, SpeakerCreate

class SpeakerRepository(ABC):
    @abstractmethod
    def save(self, speaker: SpeakerCreate) -> Speaker:
        pass

    @abstractmethod
    def find_by_id(self, speaker_id: str) -> Speaker:
        pass

    @abstractmethod
    def list_by_event(self, event_id: str) -> list[Speaker]:
        pass