from sqlalchemy import event

from app.infrastructure.database.models import Event
from app.infrastructure.elasticsearch.event_indexer import delete_event_from_index, index_event

def register_event_handlers():
    @event.listens_for(Event, "after_insert")
    async def after_insert(mapper, connection, target):
        await index_event(target)

    @event.listens_for(Event, "after_update")
    async def after_update(mapper, connection, target):
        await index_event(target)

    @event.listens_for(Event, "after_delete")
    async def after_delete(mapper, connection, target):
        await delete_event_from_index(target.id)