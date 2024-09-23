from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///dev.db")
session = sessionmaker(engine)

def get_session():
    yield session()