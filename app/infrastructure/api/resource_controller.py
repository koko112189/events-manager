# app/infrastructure/api/resource_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.domain.resource import ResourceCreate, ResourceResponse
from app.core.services.resource_service import ResourceService
from app.infrastructure.database.postgres_resource_repository import PostgresResourceRepository
from app.infrastructure.database.session import get_db

router = APIRouter()

@router.post("/resources", response_model=ResourceResponse, summary="Agregar un nuevo recurso", tags=["Recursos"])
def add_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    """
    Agrega un nuevo recurso.

    Parámetros:
    - **resource**: Un objeto `ResourceCreate` con la información del recurso.

    Respuesta:
    - Un objeto `ResourceResponse` con la información del recurso agregado.
    """
    try:
        repository = PostgresResourceRepository(db)
        service = ResourceService(repository)
        new_resource = service.add_resource(resource)
        return new_resource
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/events/{event_id}/resources", response_model=list[ResourceResponse], summary="Listar recursos de un evento", tags=["Recursos"])
def list_resources(event_id: str, db: Session = Depends(get_db)):
    """
    Lista todos los recursos de un evento.

    Parámetros:
    - **event_id**: El ID del evento cuyos recursos se desean listar.

    Respuesta:
    - Una lista de objetos `ResourceResponse` con la información de los recursos.
    """
    try:
        repository = PostgresResourceRepository(db)
        service = ResourceService(repository)
        resources = service.list_resources(event_id)
        return resources
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))