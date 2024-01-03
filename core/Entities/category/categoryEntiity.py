from pydantic import BaseModel
from typing import Optional
class CategoryEntity(BaseModel):
    id:int
    nombre:str
    