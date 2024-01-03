
from core.Entities.autor.autorEntity import AutorEntity
from abc import ABC,abstractmethod

class Iautor(ABC):

    @abstractmethod
    def crearAutor(self,autor:AutorEntity) ->AutorEntity: ...
    @abstractmethod
    def getAllAutores(self) ->list[AutorEntity] : ...
    @abstractmethod
    def searchAutoresByName(self,name:str): ...
    @abstractmethod
    def ActualizarCantidadLibros( self,idAutor:str ) ->bool: ...


