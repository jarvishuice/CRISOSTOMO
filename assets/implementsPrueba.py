from prueba import PRUEBA
from config.helpers.override import override
class IMPLEMENTACION(PRUEBA):
    @override
    def __init__(self):
        pass
    @override
    def getNombre(self,nombre):
        print(nombre)


x=IMPLEMENTACION()
x.getNombre(nombre="jarvis")