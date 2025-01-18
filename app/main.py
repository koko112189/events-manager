from fastapi import FastAPI
from app.config.settings import settings
from app.infrastructure.api.event_controller import router as event_router
from app.infrastructure.api.attendee_controller import router as attendee_router
from app.infrastructure.api.resource_controller import router as resource_router
from app.infrastructure.api.session_controller import router as session_router
from app.infrastructure.api.speaker_controller import router as speaker_router
from app.infrastructure.database.event_handlers import register_event_handlers
from app.infrastructure.elasticsearch.event_indexer import create_event_index
from app.utils.elasticsearch_utils import wait_for_elasticsearch

app = FastAPI(
    title="API de Mis Eventos",
    description="Una API para gestionar eventos de manera eficiente.",
    version="1.0.0",
    openapi_tags=[{
        "name": "Eventos",
        "description": "Operaciones relacionadas con la gestión de eventos."
    }]
)

app.include_router(event_router)
app.include_router(attendee_router)
app.include_router(resource_router)
app.include_router(session_router)
app.include_router(speaker_router)

register_event_handlers()
@app.on_event("startup")
async def startup_event():
    wait_for_elasticsearch(settings.ELASTICSEARCH_URL)
    await create_event_index()
    
@app.get("/", summary="Página de inicio", description="Muestra un mensaje de bienvenida.")
def read_root():
    return {"message": "Welcome to Mis Eventos!"}