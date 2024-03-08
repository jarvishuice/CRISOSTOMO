from pydantic import BaseModel


class SubCategoriaEntity(BaseModel):
    idCategoria:int
    id:int
    nombre:str