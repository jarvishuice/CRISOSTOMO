import datetime
from config.router.pahtsMunay import PathMunay


class Logs :
    ERROR = "\033[0;31m"
    NOTE = "\033[0;33m"
    def __inti__(self):
        print('Call  Logs')

    @staticmethod
    def WirterTask(mensaje):
        try:
            with open(f'{PathMunay().getLogs()}systemLog.log', 'a') as archivo :
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;32m{mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividasdes')
            print(error)
    @staticmethod
    def Warnings(mensaje:str):
        try:
            with open(f'{PathMunay().getLogs()}systemLog.log', 'a') as archivo :
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;33m {mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividades')
    @staticmethod
    def Error( mensaje:str):
        try:
            with open(f'{PathMunay().getLogs()}systemLog.log', 'a') as archivo :
                archivo.write(f' \033[0;36m[{datetime.datetime.now()}]:\033[0;31m {mensaje}\n')
                archivo.close()
        except TypeError as error:
            print('error al iniciar los logs de actividades')
    def __del__(self) -> object:
        print('cerrando los logs')
