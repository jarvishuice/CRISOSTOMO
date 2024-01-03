from abc import ABC, abstractmethod
from core.Entities.reaccion.reaccionEntity import ReaccionEntity
from core.Entities.reaccion.reaccionDetailEntity import ReaccionDetailEntity

class Ireaccion(ABC):

    @abstractmethod
    def crearReaccion(self, react: ReaccionEntity) -> ReaccionEntity: ...

    @abstractmethod
    def getAllReaccion(self) -> list[ReaccionDetailEntity]: ...

    @abstractmethod
    def getReaccionToday(self) -> list[ReaccionDetailEntity]: ...

    @abstractmethod
    def filterReaccionByLibro(self, idLibro: str) -> list[ReaccionDetailEntity]: ...

    @abstractmethod
    def filterReaccionByUsuario(self, idUsuario: str) -> list[ReaccionDetailEntity]: ...

    @abstractmethod
    def countReactionBylibro(self, idLibro: str) -> int: ...

    @abstractmethod
    def countReactionByUser(self, idUser: str) -> int: ...
