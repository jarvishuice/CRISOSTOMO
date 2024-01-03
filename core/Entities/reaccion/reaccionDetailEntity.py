from pydantic import BaseModel
from typing import Optional


class ReaccionDetailEntity(BaseModel):
    libro: str
    usuario:str
    fecha:str