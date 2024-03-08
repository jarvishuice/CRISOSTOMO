from Core.Entities.Autor.AutorEntity import AutorEntity
from Core.Entities.ResponseINternalEntity import ResponseInternalEntity
from Core.ROOM.ResponseInternal import ResponseInternal
from Core.interface.IAutor.IAutor import IAutor
from config.LOGS.LogsSystem import Logs
from providers.Db.PostgresConection import Psql



class AutorDAO(IAutor,Logs,Psql):
    def __init__ (self) :
        super ().__init__ ()
    def CrearAutor (self, autor: AutorEntity) :

            data = [ ]
            try :
                conexion = self.connect ()
                if conexion.status == False :
                    self.Error ("error de conexion a la base de datos")
                    return ResponseInternalEntity (status=False,
                                                   message="Erro de conexion al servidor de base de datos",
                                                   response=data)
                with self.conn.cursor () as cur :
                    cur.execute (f"""INSERT INTO public.autores (id, nombre, apellido, cantidad_libros) 
                    VALUES('{autor.id}', '{autor.nombre}', '{autor.apellido}', 0);""")
                    self.conn.commit()
                    self.WirterTask("autor registrado")
                    return ResponseInternalEntity (status=True,
                                                   message="Autor registrado",
                                                   response=data)
            except self.INTEGRIDAD_ERROR as e :
                Logs.Error(f"error de integirdad en la base de datos detail[{e}]")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False,
                                            message="error de integridad por favor valide los datos",
                                            response=None))
            except self.DATABASE_ERROR as e :
                Logs.Error (f"Error de base de datos  detail[{e}]")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message="error de base de datos", response=None))
            except self.INTERFACE_ERROR as e :
                Logs.Error (f"Error de interface detail {e}")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message="Error de interface en base de datos", response=None))
            except self.OPERATIONAL_ERROR as e :
                Logs.Error (f"Error de operaciones detail [{e}]")
                return ResponseInternal.responseInternal (
                    ResponseInternalEntity (status=False, message="Error de operaciones en la base de datos",
                                            response=None))
            finally :
                self.disconnect ()


    def getAllAutor (self) :
        pass

    def searchAutorByName (self) :
        pass



