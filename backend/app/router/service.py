from fastapi import APIRouter, Depends, HTTPException
from app.crud.service import get_services, service_by_id
from app.connection import get_session
from sqlalchemy.orm import Session
from app.schemas.service import ServiceResponse, SubDataResponse, SunDataCreate
from typing import List

service_router = APIRouter(prefix='/service')
@service_router.get("/")
async def get_service(db: Session = Depends(get_session)):
    return get_services(db)


@service_router.get("/{service_id}", response_model=ServiceResponse)
async def get_service_by_id(service_id: int, db: Session = Depends(get_session)):
    service = service_by_id(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


# @service_router.post("/category")
# async def create_category(data: SunDataCreate, db: Session = Depends(get_session)): 
    
