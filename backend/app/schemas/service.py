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
    frame_work: SubDataResponse
    database: SubDataResponse
    starting_price: int