from pydantic import BaseModel
from typing import Optional
class LibrosEntity(BaseModel):
    """
    :var id:Optional[str]
    :var titulo: str
    :var idAutor:str
    :var idCategoria:int
    :var idStatus:int
    :var fPublicacion:str
    :var idUserPublish:str
    :var idEditorial:str
    :var descargas:int
    :var archivoNombre:str
    """
    id: Optional[str]
    titulo: str
    idAutor: str
    idCategoria: int
    idStatus: int
    fPublicacion: str
    idUserPublish: str
    idEditorial:str
    descargas:int
    archivoNombre:str
