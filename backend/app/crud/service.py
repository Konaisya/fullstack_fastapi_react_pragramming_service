from app.models import Service, FrameWork, ProgrammingLanguage, DataBase, Category
from sqlalchemy.orm import Session

def get_services(db: Session):
    results = db.query(
        Service.name.label('service_name'),
        FrameWork.name.label('framework_name'),
        ProgrammingLanguage.name.label('programming_language_name'),
        DataBase.name.label('database_name'),
        Service.starting_price.label('starting_price')
    ).join(FrameWork, FrameWork.id == Service.framework_id) \
     .join(ProgrammingLanguage, ProgrammingLanguage.id == Service.programming_language_id) \
     .join(DataBase, DataBase.id == Service.database_id) \
     .all()

    return [
        {
            'service_name': service_name,
            'framework_name': framework_name,
            'programming_language_name': programming_language_name,
            'database_name': database_name, 
            'starting_price': starting_price
            
        }
        for service_name, framework_name, programming_language_name, database_name, starting_price in results
    ]


def get_programming_language_filter_by(db: Session, **filter_by):
    return db.query(ProgrammingLanguage).filter_by(**filter_by).all()

def get_category_filter_by(db: Session, **filter_by):
    return db.query(Category).filter_by(**filter_by).all()

def get_framework_filter_by(db: Session, **filter_by):
    return db.query(FrameWork).filter_by(**filter_by).all()

def get_database_filter_by(db: Session, **filter_by):
    return db.query(DataBase).filter_by(**filter_by).all()

def service_by_id(db: Session, service_id: int):
    return db.query(Service).filter(Service.id == service_id).first()

def create_category(db: Session, category_name: str):
    category = Category(name=category_name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def create_programming_language(db: Session, programming_language_name: str):
    programming_language = ProgrammingLanguage(name=programming_language_name)
    db.add(programming_language)
    db.commit()
    db.refresh(programming_language)
    return programming_language

def create_framework(db: Session, framework_name: str):
    framework = FrameWork(name=framework_name)
    db.add(framework)
    db.commit()
    db.refresh(framework)
    return framework

def create_database(db: Session, database_name: str):
    database = DataBase(name=database_name)
    db.add(database)
    db.commit()
    db.refresh(database)
    return database


def create_service (db: Session, data:dict):
    service = Service(**data)
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

def delete_category(db: Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        return False
    db.delete(category)
    db.commit()
    return True

def delete_programming_language(db: Session, programming_language_id: int):
    programming_language = db.query(ProgrammingLanguage).filter(ProgrammingLanguage.id == programming_language_id).first()
    if not programming_language:
        return False
    db.delete(programming_language)
    db.commit()
    return True

def delete_framework(db: Session, framework_id: int):
    framework = db.query(FrameWork).filter(FrameWork.id == framework_id).first()
    if not framework:
        return False
    db.delete(framework)
    db.commit()
    return True


def delete_database(db: Session, database_id: int):
    database = db.query(DataBase).filter(DataBase.id == database_id).first()
    if not database:
        return False
    db.delete(database)
    db.commit()
    return True


def delete_service(db: Session, service_id: int):
    service = db.query(Service).filter(Service.id == service_id).delete()
    if service:
        db.commit()
        return True

def put_category (db: Session, category_id: int, category_name: str):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        return False
    category.name = category_name
    db.commit()
    return category

def put_programming_language (db: Session, programming_language_id: int, programming_language_name: str):
    programming_language = db.query(ProgrammingLanguage).filter(ProgrammingLanguage.id == programming_language_id).first()
    if not programming_language:
        return False
    programming_language.name = programming_language_name
    db.commit()
    return programming_language

def put_framework (db: Session, framework_id: int, framework_name: str):
    framework = db.query(FrameWork).filter(FrameWork.id == framework_id).first()
    if not framework:
        return False
    framework.name = framework_name
    db.commit()
    return framework

def put_database (db: Session, database_id: int, database_name: str):
    database = db.query(DataBase).filter(DataBase.id == database_id).first()
    if not database:
        return False
    database.name = database_name
    db.commit()
    return database

def put_service (db: Session, service_id: int, data:dict):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        return False
    for key, value in data.items():
        setattr(service, key, value)
    db.commit()
    return service