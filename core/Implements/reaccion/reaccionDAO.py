import datetime
from core.Interface.reaccion.Ireaccion import Ireaccion, ReaccionEntity, ReaccionDetailEntity
from core.config.ResponseInternal import ResponseInternal
from config.helpers.override import override
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from config.Logs.LogsActivity import Logs


class ReaccionDAO(Ireaccion, ConectionsPsqlInterface, Logs):
    def __init__(self):
        super().__init__()

    @override
    def crearReaccion(self, react: ReaccionEntity) -> object | ReaccionEntity:
        try:
            react.fecha = str(datetime.datetime.now())
            conexion: dict = self.connect()
            if conexion['status']:
                with self.conn.cursor() as cur:
                    cur.execute(
                        f"""INSERT INTO public.reacciones (id_libro, id_user, fecha) VALUES('{react.idLibro}', 
                        '{react.idUser}', '{react.fecha}');""")
                self.conn.commit()
                return ResponseInternal.responseInternal(True,
                                                         f"REaccion del usuario:[{react.idUser}] "
                                                         f"registrada con exito ", react)
            else:
                self.Error("Error de Conexion a la base de datos")
                return ResponseInternal.responseInternal(False, "error de conexion hacia bd", None)
        except self.INTEGRIDAD_ERROR as e:
            self.Error(f"se ha presentado un error de integridad en la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                     "Puede que estes registrando una reaccion cuyos datos"
                                                     " ya se encuentranregistrado !!", None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.Warnings("Finalizada la ejecucion del core reaccion  en la implementacion crear ")
            self.disconnect()

    @override
    def getAllReaccion(self) -> list[ReaccionDetailEntity] | object:
        try:
            data = []
            conexion = self.connect()
            if conexion['status']:
                with self.conn.cursor() as cur:
                    cur.execute(f"""select  l.titulo, u.user_name  , r.fecha from reacciones r 
                                     inner join libros l on l.titulo = l.titulo
                                     inner join \"user\" u on u.user_name = user_name 
                                     where u.ci = r.id_user and l.id = r.id_libro 
                                     order by r.fecha desc;""")
                    count = cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(ReaccionDetailEntity(libro=str(i[0]), usuario=str(i[1]), fecha=str(i[2])))
                        return ResponseInternal.responseInternal(True, f"se encontraron [{count}] reacciones ", data)
                    else:
                        self.Error("NO se encontraron regostros de reacciones ")
                        return ResponseInternal.responseInternal(True, "No s enecontraron registros", data)
            else:
                self.Error("Error de Conexion a la base de datos")
                return ResponseInternal.responseInternal(False, "error de conexion hacia bd", None)
        except self.INTEGRIDAD_ERROR as e:
            self.Error(f"se ha presentado un error de integridad en la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                     "Puede que estes registrando una reaccion cuyos datos ya "
                                                     "se encuentranregistrado !!", None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.Warnings("Finalizada la ejecucion del core reaccion  en la implementacion getAll")
            self.disconnect()

    def getReaccionToday(self) -> list[ReaccionEntity]:
        pass

    @override
    def filterReaccionByLibro(self, idLibro: str) -> list[ReaccionEntity] | object:
        try:
            data = []
            conexion = self.connect()
            if conexion['status']:
                with self.conn.cursor() as cur:
                    cur.execute(f"""select  l.titulo, u.user_name  , r.fecha from reacciones r 
                                     inner join libros l on l.titulo = l.titulo
                                     inner join \"user\" u on u.user_name = user_name 
                                     where u.ci = r.id_user and l.id = r.id_libro and l.id= '{idLibro}'  order by r.fecha desc;""")
                    count = cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(ReaccionDetailEntity(libro=str(i[0]), usuario=str(i[1]), fecha=str(i[2])))
                        return ResponseInternal.responseInternal(True, f"se encontraron [{count}] reacciones ", data)
                    else:
                        self.Error("NO se encontraron regostros de reacciones ")
                        return ResponseInternal.responseInternal(True, "No s enecontraron registros", data)
            else:
                self.Error("Error de Conexion a la base de datos")
                return ResponseInternal.responseInternal(False, "error de conexion hacia bd", None)
        except self.INTEGRIDAD_ERROR as e:
            self.Error(f"se ha presentado un error de integridad en la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                     "Puede que estes registrando una reaccion cuyos datos ya "
                                                     "se encuentranregistrado !!", None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.Warnings("Finalizada la ejecucion del core reaccion  en la implementacion getAll")
            self.disconnect()

    def filterReaccionByUsuario(self, idUsuario: str) -> list[ReaccionEntity] | object:
        try:
            data = []
            conexion = self.connect()
            if conexion['status']:
                with self.conn.cursor() as cur:
                    cur.execute(f"""select  l.titulo, u.user_name  , r.fecha from reacciones r 
                                     inner join libros l on l.titulo = l.titulo
                                     inner join \"user\" u on u.user_name = user_name 
                                     where u.ci = r.id_user and l.id = r.id_libro and r.id_usuario='{idUsuario}' ;""")
                    count = cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(ReaccionDetailEntity(libro=str(i[0]), usuario=str(i[1]), fecha=str(i[2])))
                        return ResponseInternal.responseInternal(True, f"se encontraron [{count}] reacciones ", data)
                    else:
                        self.Error("NO se encontraron regostros de reacciones ")
                        return ResponseInternal.responseInternal(True, "No s enecontraron registros", data)
            else:
                self.Error("Error de Conexion a la base de datos")
                return ResponseInternal.responseInternal(False, "error de conexion hacia bd", None)
        except self.INTEGRIDAD_ERROR as e:
            self.Error(f"se ha presentado un error de integridad en la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                     "Puede que estes registrando una reaccion cuyos datos "
                                                     "ya se encuentranregistrado !!", None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.Warnings("Finalizada la ejecucion del core reaccion  en la implementacion getAll")
            self.disconnect()

    def countReactionBylibro(self, idLibro: str) -> int | object:
        try:
            data = []
            conexion = self.connect()
            if conexion['status']:
                with self.conn.cursor() as cur:
                    cur.execute(f"""select  count(id_user) from reacciones where id_libro = '{idLibro}' ;""")
                    count = cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(i)
                        return ResponseInternal.responseInternal(True, f"se encontraron [{count}] reacciones ", data[0])
                    else:
                        self.Error("NO se encontraron regostros de reacciones ")
                        return ResponseInternal.responseInternal(True, "No s enecontraron registros", data)
            else:
                self.Error("Error de Conexion a la base de datos")
                return ResponseInternal.responseInternal(False, "error de conexion hacia bd", None)
        except self.INTEGRIDAD_ERROR as e:
            self.Error(f"se ha presentado un error de integridad en la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                     "Puede que estes registrando una reaccion cuyos datos ya "
                                                     "se encuentranregistrado !!", None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.Warnings("Finalizada la ejecucion del core reaccion  en la implementacion getAll")
            self.disconnect()

    def countReactionByUser(self, idUser: str) -> int | object:
        try:
            data = []
            conexion = self.connect()
            if conexion['status']:
                with self.conn.cursor() as cur:
                    cur.execute(f"""select  count(id_user) from reacciones where id_user = '{idUser}'""")
                    count = cur.rowcount
                    if count > 0:
                        for i in cur:
                            data.append(i)
                        return ResponseInternal.responseInternal(True, f"se encontraron [{count}] reacciones ", data[0])
                    else:
                        self.Error("NO se encontraron regostros de reacciones ")
                        return ResponseInternal.responseInternal(True, "No s enecontraron registros", data)
            else:
                self.Error("Error de Conexion a la base de datos")
                return ResponseInternal.responseInternal(False, "error de conexion hacia bd", None)
        except self.INTEGRIDAD_ERROR as e:
            self.Error(f"se ha presentado un error de integridad en la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,
                                                     "Puede que estes registrando una reaccion cuyos datos ya "
                                                     "se encuentranregistrado !!", None)
        except self.INTERFACE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e:
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)

        finally:
            self.Warnings("Finalizada la ejecucion del core reaccion  en la implementacion getAll")
            self.disconnect()
