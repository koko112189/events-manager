from fastapi import FastAPI
from app.infrastructure.api.event_controller import router as event_router

app = FastAPI(
    title="API de Mis Eventos",
    description="Una API para gestionar eventos de manera eficiente.",
    version="1.0.0",
    openapi_tags=[{
        "name": "Eventos",
        "description": "Operaciones relacionadas con la gestión de eventos."
    }]
)

# Registrar rutas
app.include_router(event_router)

@app.get("/", summary="Página de inicio", description="Muestra un mensaje de bienvenida.")
def read_root():
    return {"message": "Welcome to Mis Eventos!"}