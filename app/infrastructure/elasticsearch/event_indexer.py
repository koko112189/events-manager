# app/infrastructure/elasticsearch/event_index.py
from fastapi import HTTPException
from python_http_client import NotFoundError
from app.infrastructure.elasticsearch.client import elasticsearch_client as es

async def create_event_index():
    index_name = "events"
    if not await es.indices.exists(index=index_name):
        await es.indices.create(
            index=index_name,
            body={
                "mappings": {
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "text"},
                    }
                }
            },
            ignore=400,  # Ignorar si el índice ya existe
        )

async def index_event(event):
    await es.index(
        index="events",
        id=event.id,
        body={
            "id": event.id,
            "name": event.name,
        },
    )

async def delete_event_from_index(event_id):
    await es.delete(index="events", id=event_id, ignore=404) 

async def search_events(query: str):
    try:
        response = await es.search(
            index="events",
            body={
                "query": {
                    "multi_match": {
                        "query": query,
                        "fields": ["name"],
                    }
                }
            },
        )
        return [hit["_source"] for hit in response["hits"]["hits"]]           
    except NotFoundError:
        return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))