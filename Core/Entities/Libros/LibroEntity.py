from pydantic import BaseModel


class LibrosEntity(BaseModel):
    id:str
    titulo:str
    idAutor:str
    idCategoria:int
    fPublicacion:str
    idUser:str
    idEditorial:str
    path:str
    idSubCategoria:int
    descargas:int

