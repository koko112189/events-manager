from fastapi import FastAPI
from app.infrastructure.api.event_controller import router as event_router

app = FastAPI()

# Registrar rutas
app.include_router(event_router)

@app.get("/")
def read_root():
    return {"message": "Welcome "}