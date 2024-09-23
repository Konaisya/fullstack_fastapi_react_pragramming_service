from app.models import Service, FrameWork, ProgrammingLanguage, DataBase
from sqlalchemy.orm import Session

def get_services(db: Session):
    return db.query(Service).join(FrameWork, FrameWork.id == Service.framework_id).join(ProgrammingLanguage, ProgrammingLanguage.id == Service.programming_language_id).join(DataBase, DataBase.id == Service.database_id).all()

def service_by_id(db: Session, service_id: int):
    return db.query(Service).filter(Service.id == service_id).first()

def create_category(db: Session, category_name: str):
    category = Category(name=category_name)


