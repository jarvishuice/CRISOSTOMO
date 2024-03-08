from pydantic import BaseModel


class AutorEntity(BaseModel):
    id:str
    nombre:str
    apellido:str
    cantidadLibros:int