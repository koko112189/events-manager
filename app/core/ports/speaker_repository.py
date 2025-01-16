from abc import ABC, abstractmethod
from app.core.domain.speaker import SpeakerCreate, SpeakerRead

class SpeakerRepository(ABC):
    @abstractmethod
    def save(self, speaker: SpeakerCreate) -> SpeakerCreate:
        pass

    @abstractmethod
    def find_by_id(self, speaker_id: int) -> SpeakerRead:
        pass

    @abstractmethod
    def list_by_event(self, event_id: int) -> list[SpeakerRead]:
        pass