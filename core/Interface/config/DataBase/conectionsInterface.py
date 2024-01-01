from abc import ABC, abstractmethod

class ConectionDbInterface(ABC):
    ERROR="\033[0;31m"
    NOTE="\033[0;33m"
    DATABASE_ERROR=None
    INTEGRIDAD_ERROR=None
    INTERFACE_ERROR=None
    OPERATIONAL_ERROR=None

    @abstractmethod
    def connect(self):
        pass

    def disconnect(self):
        pass

    def wirter(self, data) -> dict:
        pass

    def readAll(self) -> dict:
        pass
    def readOneById(self, id ) -> dict:
        pass

    def search(self,param)->dict:
        pass
    # read one register by param
    def readOneByParam(self,param) ->dict:
        pass
    #read all by status
    def readOneByStatus(self,status)-> dict:
        pass
    def readAllTwoParm(self,param,param2)-> dict:
        pass
    #lectura de todos los detalles de la entidad vinculada en distintas tablas
    def readDetailEntity(self,id)-> dict:
        pass
    #actualizar la cantidad de un campo por un id
    def  updateCantidadById(self,id,catidad,sede)-> dict :
        pass