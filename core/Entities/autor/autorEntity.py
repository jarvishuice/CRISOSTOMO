from pydantic import BaseModel
from typing import Optional

class AutorEntity(BaseModel):
    id:Optional[str]
    nombre:str
    apellido:str
    cantidadLibros:int
    