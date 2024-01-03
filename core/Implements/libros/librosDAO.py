import datetime
import time

from core.Entities.libros.librosEntity import LibrosEntity
from core.Interface.libros.Ilibros import Ilibros
from core.config.ResponseInternal import ResponseInternal
from config.helpers.override import  override
from config.Db.conectionsPsqlInterface import ConectionsPsqlInterface
from config.Logs.LogsActivity import Logs
class LibrosDAO(Ilibros,ConectionsPsqlInterface,):

    def __init__(self):
        super().__init__()
        self.logs=Logs
    @override
    def crearLibro(self,libro:LibrosEntity) -> LibrosEntity:
        try:

            conection =self.connect()
            if conection['status']==True:
                libro.id=str(time.time())
                with self.conn.cursor()as cur :
                    cur.execute(f" INSERT INTO public.libros (id, titulo, id_autor, id_categoria, id_status, "
                                f"f_publicacion, id_user_publish, id_editorial, descargas, archivo_nombre) "
                                f"VALUES('{libro.id}', '{libro.titulo}', '{libro.idAutor}', {libro.idCategoria}, "
                                f"{libro.idStatus}, 'now()', '{libro.idUserPublish}', '{libro.idEditorial}', "
                                f"{libro.descargas}, '{libro.archivoNombre}'); ")
                    self.conn.commit()
                return ResponseInternal.responseInternal(True,f"Libro publicado de manera exitosa" f" bajo el id [{libro.id}]",libro)
            else:
                self.logs.Error("Error de conexion a la base de datos en ;a implentacion de CreateLibro"
                                " del core de libros")
                return ResponseInternal.responseInternal(False,"error de conexion a la base de datos",None)
        except self.INTEGRIDAD_ERROR as e :
            self.logs.Error(f"se ha presentado un error de onmtegridad e la base de datos detail [{e}]")
            return ResponseInternal.responseInternal(False,"Puede que estes registrando un libro cuyos datos ya se encuentranregistrado !!",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)
        finally :
            self.disconnect()
    @override
    def getAllLibros (self) -> list[LibrosEntity] :
        try:
            data=[]
            conection =self.connect()
            if conection['status']==True:
                with self.conn.cursor()as cur :
                    cur.execute(" select * from libros order by f_publicacion desc ")
                    count  = cur.rowcount
                    if count > 0:
                        for i in cur :
                            libro=LibrosEntity(id=i[0],titulo=i[1],idAutor=i[2],idCategoria=int(i[3]),
                                               idStatus=int(i[4]),fPublicacion=str(i[5]),
                                               idUserPublish=str(i[6]),idEditorial=i[7],descargas=int(i[8]),
                                               archivoNombre=i[9])
                            data.append(libro)
                        return ResponseInternal.responseInternal(True,f"EXITO AL LEER TODOS LOS "
                                                                      f"LIBROS SE ENCONTRARON [{count}] libros  ",data)
                    else:
                        self.logs.Warnings("no se encontraron registros al intentar extraer todos lo libros ")
                        return ResponseInternal.responseInternal(True,"no se encontraron registros",data)

            else:
                self.logs.Error("Error de conexion a la base de datos en ;a implentacion de CreateLibro"
                                " del core de libros")
                return ResponseInternal.responseInternal(False,"error de conexion a la base de datos",None)
        except self.INTERFACE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error de interface {e}")
            return ResponseInternal.responseInternal(False, "ERROR de interface en la base de datos ", None)
        except self.DATABASE_ERROR as e :
            Logs.WirterTask(f"{self.ERROR} error en la base de datos detail{e}")
            return ResponseInternal.responseInternal(False, "ERROR EN LA BASE DE DATOS", None)
        finally :
            self.disconnect()

    def filterLibrosByAutor (self, autor: str) -> list[LibrosEntity] :
        pass

    def filterLibrosByCategoria (self, categoria: int) :
        pass

    def searchLibro (self, titulo: str) -> list[LibrosEntity] :
        pass

    def filterLibrosByEditorial (self, editorial: str) -> list[LibrosEntity] :
        pass
