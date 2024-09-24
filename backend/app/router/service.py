from fastapi import APIRouter, Depends, HTTPException
from app.crud.service import *
from app.connection import get_session
from sqlalchemy.orm import Session
from app.schemas.service import *
from typing import List

service_router = APIRouter(prefix='/service', tags=['Service'])
@service_router.get("/")
async def get_service(db: Session = Depends(get_session)):
    return get_services(db)

@service_router.get("/category")
async def get_category_all_service(db: Session = Depends(get_session)):
    categories =  get_category_filter_by(db)
    return [SubDataResponse(id = category.id, name = category.name) for category in categories]

@service_router.get("/programming_language")
async def get_programming_language_all_service(db: Session = Depends(get_session)):
    programming_languages =  get_programming_language_filter_by(db)
    return [SubDataResponse(id = programming_language.id, name = programming_language.name) for programming_language in programming_languages]

@service_router.get("/database")
async def get_database_all_service(db: Session = Depends(get_session)):
    databases =  get_database_filter_by(db)
    return [SubDataResponse(id = database.id, name = database.name) for database in databases]

@service_router.get("/framework")
async def get_framework_all_service(db: Session = Depends(get_session)):
    frameworks =  get_framework_filter_by(db)
    return [SubDataResponse(id = framework.id, name = framework.name) for framework in frameworks]


@service_router.get("/category/{category_id}")
async def get_category_by_id_service(category_id: int, db: Session = Depends(get_session)):
    category = get_category_filter_by(db, id = category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category[0]

@service_router.get("/framework/{framework_id}")
async def get_framework_by_id_service(framework_id: int, db: Session = Depends(get_session)):
    framework = get_framework_filter_by(db, id = framework_id)
    if not framework:
        raise HTTPException(status_code=404, detail="Framework not found")
    return framework[0]

@service_router.get("/programming_language/{programming_language_id}")
async def get_programming_language_by_id_service(programming_language_id: int, db: Session = Depends(get_session)):
    programming_language = get_programming_language_filter_by(db,id = programming_language_id)
    if not programming_language:
        raise HTTPException(status_code=404, detail="Programming language not found")
    return programming_language[0]

@service_router.get("/database/{database_id}")
async def get_database_by_id_service(database_id: int, db: Session = Depends(get_session)):
    database = get_database_filter_by(db,id = database_id )
    if not database:
        raise HTTPException(status_code=404, detail="Database not found")
    return database[0]


@service_router.get("/{service_id}")
async def get_service_by_id(service_id: int, db: Session = Depends(get_session)):
    service = service_by_id(db, service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@service_router.post("/category")
async def create_category_service(data: SunDataCreate, db: Session = Depends(get_session)): 
    category = create_category(db, data.name)
    return category
    
@service_router.post("/programming_language")
async def create_programming_language_service(data: SunDataCreate, db: Session = Depends(get_session)):
    programming_language = create_programming_language(db, data.name)
    return programming_language

@service_router.post("/database")
async def create_database_service(data: SunDataCreate, db: Session = Depends(get_session)):
    database = create_database(db, data.name)
    return database

@service_router.post("/framework")
async def create_framework_service(data: SunDataCreate, db: Session = Depends(get_session)):
    framework = create_framework(db, data.name)
    return framework

@service_router.post("/")
async def create_service_service( data: ServiceCreate, db: Session = Depends(get_session)):
    service = create_service(db, data.model_dump())
    return service

@service_router.put("/category/{category_id}")
async def put_category_by_id_service(category_id: int, data: SunDataCreate, db: Session = Depends(get_session)):
    category = put_category(db, category_id, data.name)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"massage": "Success"}

@service_router.put("/framework/{framework_id}")
async def put_framework_by_id_service(framework_id: int, data: SunDataCreate, db: Session = Depends(get_session)):
    framework = put_framework(db, framework_id, data.name)
    if not framework:
        raise HTTPException(status_code=404, detail="Framework not found")
    return {"massage": "Success"}

@service_router.put("/programming_language/{programming_language_id}")
async def put_programming_language_by_id_service(programming_language_id: int, data: SunDataCreate, db: Session = Depends(get_session)):
    programming_language = put_programming_language(db, programming_language_id, data.name)
    if not programming_language:
        raise HTTPException(status_code=404, detail="Programming language not found")
    return {"massage": "Success"}

@service_router.put("/database/{database_id}")
async def put_database_by_id_service(database_id: int, data: SunDataCreate, db: Session = Depends(get_session)):
    database = put_database(db, database_id, data.name)
    if not database:
        raise HTTPException(status_code=404, detail="Database not found")
    return {"massage": "Success"}

@service_router.put("/{service_id}")
async def put_service_by_id_service(service_id: int, data: ServiceCreate, db: Session = Depends(get_session)):
    service = put_service(db, service_id, data.model_dump())
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"massage": "Success"}

@service_router.delete("/category/{category_id}")
async def delete_category_by_id_service(category_id: int, db: Session = Depends(get_session)):
    deleted = delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"deleted": deleted}

@service_router.delete("/database/{database_id}")
async def delete_database_by_id_service(database_id: int, db: Session = Depends(get_session)):
    deleted = delete_database(db, database_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Database not found")
    return {"deleted": deleted}

@service_router.delete("/framework/{framework_id}")
async def delete_framework_by_id_service(framework_id: int, db: Session = Depends(get_session)):
    deleted = delete_framework(db, framework_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Framework not found")
    return {"deleted": deleted}

@service_router.delete("/programming_language/{programming_language_id}")
async def delete_programming_language_by_id_service(programming_language_id: int, db: Session = Depends(get_session)):
    deleted = delete_programming_language(db, programming_language_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Programming language not found")
    return {"deleted": deleted}

@service_router.delete("/category/{category_id}")
async def delete_category_by_id_service(category_id: int, db: Session = Depends(get_session)):
    deleted = delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"deleted": deleted}

@service_router.delete("/{service_id}")
async def delete_service_by_id_service(service_id: int, db: Session = Depends(get_session)):
    deleted = delete_service(db, service_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"massage": "Success"}