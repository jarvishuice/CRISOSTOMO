
 
class PathMunay:
    root = None
    logs = None
    
    def __init__(self):
        self.root = '/home/jarvis/PycharmProjects/CRISOSTOMO'
        self.logs = f'{self.root}/Logs/'

    def getRoot(self) -> str:
        
        return self.root
    def getLogs(self) -> str:
        """

        :return: str
        """
        return self.logs
    
 
