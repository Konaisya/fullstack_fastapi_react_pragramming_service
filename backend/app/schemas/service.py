from pydantic import BaseModel


class SubDataResponse(BaseModel):
    id: int
    name: str


class SunDataCreate(BaseModel):
    name: str


class ServiceResponse(BaseModel):
    id: int
    name: str
    category: SubDataResponse
    programming_language: SubDataResponse
    framework: SubDataResponse
    database: SubDataResponse
    starting_price: int

class ServiceCreate(BaseModel):
    name: str
    category_id: int
    programming_language_id: int
    framework_id: int
    database_id: int
    starting_price: int

