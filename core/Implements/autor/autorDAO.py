import time
from core.config.ResponseInternal import ResponseInternal
from config.helpers.override import  override
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from config.Logs.LogsActivity import Logs
from core.Interface.autor.Iautor import Iautor,AutorEntity
class AutorDAO(Iautor,ConectionsPsqlInterface):
    def __init__(self):
        super().__init__()
        self.logs = Logs()
    @override
    def crearAutor(self,autor:AutorEntity) -> AutorEntity:
        try:
            conection = self.connect()
            autor.id = str(time.time())
            if conection['status'] == True:
                with self.conn.cursor() as cur:
                    cur.execute(f"INSERT INTO public.autores (id, nombre, apellido, cantidad_libros) "
                                f"VALUES('{autor.id}', '{autor.nombre}', '{autor.apellido}',{autor.cantidadLibros});")
                self.conn.commit()
                return ResponseInternal.responseInternal(True,f"Autor registrado con exito{dict(autor)}",autor)
            else:
                self.logs.Error("error de conexion en la base de datos ")
                return ResponseInternal.responseInternal(True,"Error de conexion En bd",None)
        except self.INTEGRIDAD_ERROR as e:
            self.logs.Error(f"se ha presentado un error de onmtegridad e la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                         "Puede que estes registrando un author cuyos datos "
                                                         "ya se encuentran registrado !!",
                                                         None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)
        finally :
            self.disconnect()

    @override
    def getAllAutores (self) -> list[AutorEntity] :
        try:
            data = []
            conection = self.connect()
            if conection['status'] == True:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT * FROM  autores ORDER BY id DESC ;")
                    count = cur.rowcount
                    if count  > 0:
                        for i in cur:
                            data.append(AutorEntity(id=i[0], nombre=i[1], apellido=i[2], cantidadLibros=int(i[3])))

                        return ResponseInternal.responseInternal(True,f" lectura de autors realizadsa con exito "
                                                              f"se encontraron [{count}] autores",data)
                    else :
                        self.logs.Error("No se encontraron regfistros de autores ")
                        return ResponseInternal.responseInternal(True,"no se enciantraron regsitros",data)
            else:
                self.logs.Error("error de conexion en la base de datos ")
                return ResponseInternal.responseInternal(True,"Error de conexion En bd",None)
        except self.INTEGRIDAD_ERROR as e:
            self.logs.Error(f"se ha presentado un error de onmtegridad e la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                         "Puede que estes registrando un author cuyos datos "
                                                         "ya se encuentran registrado !!",
                                                         None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)
        finally :
            self.disconnect()


    @override
    def searchAutoresByName (self, name: str) -> list[AutorEntity]:
        try :
            data = []
            conection = self.connect()
            if conection['status'] == True :
                with self.conn.cursor() as cur :
                    cur.execute(f"SELECT * FROM  autores  where nombre ilike '%{name}%' ORDER BY id DESC ;")
                    count = cur.rowcount
                    if count > 0 :
                        for i in cur :
                            data.append(AutorEntity(id=i[0], nombre=i[1], apellido=i[2], cantidadLibros=int(i[3])))

                        return ResponseInternal.responseInternal(True, f" lectura de autors realizadsa con exito "
                                                               f"se encontraron [{count}] autores", data)
                    else:
                        self.logs.Warnings(f"no se encontraron coinceidencias en authores con el nombre {name}")
                        return  ResponseInternal.responseInternal(True,f"no se encontraron coincidencia "
                                                                       f"con el nombre {name}",data)
            else :
                self.logs.Error("error de conexion en la base de datos ")
                return ResponseInternal.responseInternal(True, "Error de conexion En bd", None)
        except self.INTEGRIDAD_ERROR as e :
            self.logs.Error(f"se ha presentado un error de onmtegridad e la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                     "Puede que estes registrando un author cuyos datos "
                                                     "ya se encuentran registrado !!",
                                                     None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)
        finally :
            self.disconnect()

    @override
    def ActualizarCantidadLibros (self, idAutor: str) -> bool :
        try :
            conexion = self.connect()
            if conexion['status'] == True :
                with self.conn.cursor() as cur :
                    cur.execute(f"""update autores set cantidad_libros = (select count(id) from libros where 
                                id_autor = '{idAutor}' ) where id='{idAutor}' ; """)
                    self.conn.commit()
                    count = cur.rowcount
                    if count > 0:
                        return ResponseInternal.responseInternal(True,f"""ajustado la cantidad 
                        de libros del autor#[{idAutor} ]""",True)
                    else :
                        self.logs.Warnings(f"no s eencontraron coincindencias para el author #[{idAutor}]")
                        return ResponseInternal.responseInternal(True, f"""ajustado la cantidad 
                                                de libros del autor pero no se encontraron coicicencias #[{idAutor} ]""",
                                                                 True)
            else :
                        self.logs.Error("error de conexion en la base de datos ")
                        return ResponseInternal.responseInternal(True, "Error de conexion En bd", None)
        except self.INTEGRIDAD_ERROR as e:
                self.logs.Error(f"se ha presentado un error de onmtegridad e la base de datos detail [{e}]")
                return ResponseInternal.responseInternal(False,
                                                         "Puede que estes registrando un author cuyos datos "
                                                         "ya se encuentran registrado !!",
                                                         None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)
        finally :
            self.disconnect()