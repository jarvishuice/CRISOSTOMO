from pydantic import BaseModel


class EditorialEntity(BaseModel):
    id:str
    nombre:str