from abc import ABC,abstractmethod

from Core.Entities.Autor.AutorEntity import AutorEntity


class IAutor(ABC):
    @abstractmethod
    def CrearAutor(self,autor:AutorEntity): ...
    @abstractmethod
    def getAllAutor(self): ...
    @abstractmethod
    def searchAutorByName(self): ...
    
