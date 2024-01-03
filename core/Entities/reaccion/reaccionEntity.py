from pydantic import BaseModel
from typing import Optional
class ReaccionEntity(BaseModel):
    idLibro: str
    idUser: str
    fecha : str
