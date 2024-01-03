from abc import ABC, abstractmethod


class ConectionDbInterface (ABC):
    ERROR = "\033[0;31m"
    NOTE = "\033[0;33m"
    DATABASE_ERROR = None
    INTEGRIDAD_ERROR = None
    INTERFACE_ERROR = None
    OPERATIONAL_ERROR = None

    @abstractmethod
    def connect(self):
        pass

    def disconnect(self):
        pass
