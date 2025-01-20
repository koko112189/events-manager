import pytest
from app.core.services.speaker_service import SpeakerService
from app.core.ports.speaker_repository import SpeakerRepository
from app.core.domain.speaker import Speaker, SpeakerCreate

class MockSpeakerRepository(SpeakerRepository):
    def save(self, speaker: SpeakerCreate) -> Speaker:
        return Speaker(id="1", **speaker.dict())

    def find_by_id(self, speaker_id: str) -> Speaker:
        return Speaker(id=speaker_id, name="Test Speaker", bio="Test", event_id="1")

    def list_by_event(self, event_id: str) -> list[Speaker]:
        return [Speaker(id="1", name="Test Speaker", bio="Test", event_id=event_id)]

def test_create_speaker():
    repo = MockSpeakerRepository()
    service = SpeakerService(repo)
    speaker = service.create_speaker(SpeakerCreate(name="Test Speaker", bio="Test", event_id="1"))
    assert speaker.name == "Test Speaker"

def test_get_speaker():
    repo = MockSpeakerRepository()
    service = SpeakerService(repo)
    speaker = service.get_speaker("1")
    assert speaker.id == "1"

def test_list_speakers():
    repo = MockSpeakerRepository()
    service = SpeakerService(repo)
    speakers = service.list_speakers("1")
    assert len(speakers) == 1