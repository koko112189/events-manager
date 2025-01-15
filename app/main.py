from fastapi import FastAPI
from app.infrastructure.api.event_controller import router as event_router
from app.infrastructure.api.attendee_controller import router as attendee_router
from app.infrastructure.api.resource_controller import router as resource_router

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

@app.get("/", summary="Página de inicio", description="Muestra un mensaje de bienvenida.")
def read_root():
    return {"message": "Welcome to Mis Eventos!"}