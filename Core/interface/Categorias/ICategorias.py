from abc import ABC,abstractmethod

from Core.Entities.ResponseINternalEntity import ResponseInternalEntity


class ICategorias(ABC):
    @abstractmethod
    def getAllCategoria(self)-> ResponseInternalEntity:...
    @abstractmethod
    def searchCategoriaById(self,id:int)-> ResponseInternalEntity:...
