from config.Logs.LogsActivity import Logs

class ResponseInternal():
    def __init__(self) -> None:
        pass
    @staticmethod
    def responseInternal(status:bool,mesagge:str,response):
        """
        Method that allows responding to an internal system request
        Args:
            status (bool):  State response
            mesagge (str): response message
            response (str): Response to the request

        Returns:
            dict: Diccionario con el estado, mensaje y respuesta de la peticion
        """
        Logs.WirterTask(mesagge)
        
        return{"status":status,"mesagge":mesagge,"response":response}
    
