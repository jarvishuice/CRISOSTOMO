from typing_extensions import override

from core.Entities.category.categoryEntiity import CategoryEntity
from abc import ABC,abstractmethod

from config.Logs.LogsActivity import Logs
class Icategory(ABC):

    @abstractmethod
    def crearCategria(categoria:CategoryEntity): ...
    @abstractmethod
    def getAllCategory(self) ->list[CategoryEntity] : ...
    @abstractmethod
    def searchCategoryByName(self,name:str): ...
    @abstractmethod
    def countID( self ) ->int: ...


