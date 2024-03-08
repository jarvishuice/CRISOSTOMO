from pydantic import BaseModel


class DesacargasEntity(BaseModel):
    idLibro:str
    idUser:str
    fecha:str