from Core.ROOM.ResponseInternal import ResponseInternal
from Core.interface.Categorias.ICategorias import ICategorias
from Core.Entities.Categorias.CategoriasEntity import CategoriasEntity
from providers.Db.PostgresConection import Psql,ResponseInternalEntity,Logs



class CategoriasDAO(ICategorias,Psql,Logs):


    def __init__(self):
        super().__init__()

    @property
    def getAllCategoria(self) -> ResponseInternalEntity | list[CategoriasEntity]:
        data = []
        try:
            conexion = self.connect()
            if conexion.status ==False:
                self.Error("error de conexion a la base de datos")
                return ResponseInternalEntity(status= False,
                                              message="Erro de conexion al servidor de base de datos",
                                              response=data)
            with self.conn.cursor() as cur:
                cur.execute("select * from categorias")
                if cur.rowcount <=0:
                    self.Warnings("No se encontraron registros een la tabala categorias ")
                    return ResponseInternalEntity(status=True,
                                                  message= "No se encontraron registro en la tabla categorias",
                                                  response=data)
                for i in cur :
                    data.append(CategoriasEntity(id=int(i[0]),
                                                 nombre=i[1]))
                self.WirterTask("categorias leidas con exito ")
                return ResponseInternalEntity(status= True,
                                              message= "Categorias leidas con exito",
                                              response =data)
        except self.DATABASE_ERROR as e:
            Logs.Error(f"Error de base de datos  detail[{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="error de base de datos", response=None))
        except self.INTERFACE_ERROR as e:
            Logs.Error(f"Error de interface detail {e}")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Error de interface en base de datos", response=None))
        except self.OPERATIONAL_ERROR as e:
            Logs.Error(f"Error de operaciones detail [{e}]")
            return ResponseInternal.responseInternal(
                ResponseInternalEntity(status=False, message="Error de operaciones en la base de datos", response=None))
        finally:
            self.disconnect()
    def searchCategoriaById (self, id: int) -> ResponseInternalEntity :
        pass