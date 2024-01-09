

class PathSystem:
    """
      que contiene las rutas de directorios a utilizar por el sistema
      :var root :str:  path de  crisostomo
      :var logs :str: path de los logs de  crisostomo
      :var assets str: path de los assets
      :var libros str: path de los libros
    """
    root = None
    logs = None
    assets = None
    libros = None
    
    def __init__(self):
        self.root = '/home/jarvis/PycharmProjects/CRISOSTOMO'
        self.logs = f'{self.root}/Logs/'
        self.assets = f'{self.root}/assets/'
        self.libros = f'{self.assets}/libros/'
    def getRoot(self) -> str: return self.root
    def getLogs(self) -> str: return self.logs
    def getAssets (self) -> str: return self.assets
    def getLibros(self) -> str: return self.libros
    def setRoot(self,path:str) -> str:
         self.root = path
         return self.root