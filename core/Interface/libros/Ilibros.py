from abc import ABC, abstractmethod
from core.Entities.libros.librosEntity import LibrosEntity


class Ilibros (ABC):

    @abstractmethod
    def crearLibro(self,libro:LibrosEntity) -> LibrosEntity:
        pass
    @abstractmethod
    def getAllLibros(self)-> list[LibrosEntity]:
        pass
    @abstractmethod
    def filterLibrosByAutor(self,autor:str) -> list[LibrosEntity]:
        pass
    @abstractmethod
    def filterLibrosByCategoria(self,categoria:int):
        pass
    @abstractmethod
    def searchLibro(self,titulo:str) -> list[LibrosEntity]: ...
    @abstractmethod
    def filterLibrosByEditorial(self,editorial:str) -> list[LibrosEntity]:...
