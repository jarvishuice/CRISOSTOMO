from abc import ABC,abstractmethod

from Core.Entities.Categorias.SubCategoriaEntity import SubCategoriaEntity
from Core.Entities.ResponseINternalEntity import ResponseInternalEntity


class ICategorias(ABC):
    @abstractmethod
    def getAllCategoria(self)-> ResponseInternalEntity:...
    @abstractmethod
    def searchCategoriaById(self,id:int)-> ResponseInternalEntity:...
    @abstractmethod
    def getAllSubCategorias(self)-> ResponseInternalEntity | list[SubCategoriaEntity] :...
    @abstractmethod
    def getSubCategoriaByCategoria(self,idCategoria:int) -> ResponseInternalEntity | list[SubCategoriaEntity] : ...
