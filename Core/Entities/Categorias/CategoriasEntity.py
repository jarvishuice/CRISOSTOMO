from pydantic import BaseModel


class CategoriasEntity(BaseModel):
    id:int
    nombre:str