from pydantic import BaseModel
from typing import Optional
class LibrosEntity(BaseModel):
    id:Optional[str]
    titulo:str
    idAutor:str
    idCategoria:int
    idStatus:int
    fPublicacion:str
    idUserPublish:str
    idEditorial:str
    descargas:int
    archivoNombre:str
