from core.Interface.category.Icategory import CategoryEntity,Icategory
from core.config.ResponseInternal import ResponseInternal
from config.helpers.override import  override
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from config.Logs.LogsActivity import Logs
import time
class CategoryDAO(Icategory,ConectionsPsqlInterface) :

    def __init__(self):
        self.logs: object = Logs()
        super().__init__()

    @override
    def crearCategria(self,categoria:CategoryEntity) -> CategoryEntity:
        try:
            categoria.id = self.countID()['response'] + 1
            conection = self.connect()
            if conection['status'] == True:
                with self.conn.cursor() as cur:
                    cur.execute(f"insert into categorias (id,nombre) values({categoria.id},'{categoria.nombre}')")

                self.conn.commit()
                return ResponseInternal.responseInternal(True,f"categoria registradqa de manera correcta",categoria)
            else :
                Logs.Error("error de conexion a la base de datos")
                return ResponseInternal.responseInternal(False,"error de conexion a la base de datos",None)
        except self.INTEGRIDAD_ERROR as e :
            self.logs.Error(f"se ha presentado un error de integridad en la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,"Puede que estes registrando una categoria cuyos datos ya se encuentranregistrado !!",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.logs.Warnings("Finalizada la ejecucion del core Catregoria en la implementacion crear ")
            self.disconnect()
    @override
    def countID(self)-> int:
        try:
            conexion=self.connect()
            if conexion['status'] == True:
                data=[]
                with self.conn.cursor() as cur:
                    cur.execute(f"(select count(id) from categorias ) ")
                    for i in cur :
                        h=i[0]
                        data.append(h)

                return ResponseInternal.responseInternal(True,"Categoria reistrada de manera correcta ",data[0])
            else:
                return ResponseInternal.responseInternal(False,"Error de conexion a la base de datos al crear",None)
        except self.INTEGRIDAD_ERROR as e :
            self.logs.Error(f"se ha presentado un error de onmtegridad e la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,"Puede que estes registrando un libro cuyos datos ya se encuentranregistrado !!",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.logs.Warnings("Finalizada la ejecucion de la  Implementacion Count Id  en el core category  ")
            self.disconnect()
    @override
    def getAllCategory (self) -> list[CategoryEntity] :
        data = []
        try:
            conection = self.connect()
            if conection['status'] == True:
                with self.conn.cursor() as cur :
                    cur.execute("select * from categorias")
                    count = cur.rowcount
                    if count > 0:
                        for i in cur :
                            container = CategoryEntity(id=int(i[0]),nombre=i[1])
                            data.append(container)
                        return ResponseInternal.responseInternal(True,"categorias Leidas de dmanera correcta",data)
                    else:
                        self.logs.Warning("No se encontraron registrs en la tabla categorias")
                        return ResponseInternal.responseInternal(True,"no se encintraron registros en "
                                                                      "la tablan resgister",data)
            else:
                self.logs.Error("Error de conexion  a la base de datos")
                return  ResponseInternal.responseInternal(False,"Error de conexion al servidor de BD",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.disconnect()

    @override
    def searchCategoryByName (self, name: str) :
        data = []
        try :
            conection = self.connect()
            if conection['status'] == True :
                with self.conn.cursor() as cur :
                    cur.execute(f"select * from categorias where nombre ilike '%{name}%'")
                    count = cur.rowcount
                    if count > 0 :
                        for i in cur :
                            container = CategoryEntity(id=int(i[0]), nombre=i[1])
                            data.append(container)
                        return ResponseInternal.responseInternal(True, "categorias Leidas de dmanera correcta", data)
                    else :
                        Logs.Warnings("No se encontraron registrs en la tabla categorias")
                        return ResponseInternal.responseInternal(True, "no se encintraron registros en "
                                                                       "la tablan resgister", data)
            else :
                self.logs.Error("Error de conexion  a la base de datos")
                return ResponseInternal.responseInternal(False, "Error de conexion al servidor de BD", None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally :
            self.disconnect()

