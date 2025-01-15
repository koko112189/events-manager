from elasticsearch import AsyncElasticsearch
from app.core.domain.event import Event
from app.config import settings

class ElasticsearchEventIndexer:
    def __init__(self, client: AsyncElasticsearch):
        self.client = client

    async def index_event(self, event: Event) -> None:
        await self.client.index(index="events", id=event.id, document=event.dict())