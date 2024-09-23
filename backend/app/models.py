from sqlalchemy import  ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import datetime


Base = declarative_base()

class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

class ProgrammingLanguage(Base):
    __tablename__ = "programming_language"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

class DataBase(Base):
    __tablename__ = "database"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    
class FrameWork(Base):
    __tablename__ = "framework"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

class StatusOrder(Base):
    __tablename__ = "order_status"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

    
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))



class Service(Base):
    __tablename__ = "service"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    programming_language_id: Mapped[int] = mapped_column(ForeignKey("programming_language.id"))
    database_id: Mapped[int] = mapped_column(ForeignKey("database.id"))
    framework_id: Mapped[int] = mapped_column(ForeignKey("framework.id"))
    starting_price: Mapped[int] = mapped_column(nullable=False)


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("service.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("order_status.id"))
    finally_price: Mapped[int] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    finish_date: Mapped[datetime] = mapped_column(nullable=True)


class Review(Base): 
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    rating: Mapped[int] = mapped_column(nullable=True)
    comment: Mapped[str] = mapped_column(nullable=True)