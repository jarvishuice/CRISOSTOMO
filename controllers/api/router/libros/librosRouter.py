import errno

from fastapi import APIRouter, Request,Body, HTTPException, UploadFile, File, Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.libros.librosDAO import LibrosDAO,LibrosEntity,Logs
from core.Entities.libros.librosEntity import LibrosEntity
import shutil
from pathlib import Path
from config.router.PathsSystem import PathSystem
paths = PathSystem()
core = LibrosDAO()
#security = HTTPBearer()
#validator = AuthDAO()
urlBase = "/crisostomo/"
Libros = APIRouter(prefix=f"{urlBase}Libros", tags=["Libros"])


"""def aut (credendentials: HTTPAuthorizationCredentials = Depends(security)) :
    token = credendentials.credentials
    validacion = validator.validarToken(token)
    if validacion['response'] == True :
        return True
    else :
        raise HTTPException(401, detail="token inauorizado ")
"""

""""
hay que descomentar la linea para aplicar la autenticacion
"""


@Libros.post("/create/{titulo}/{idAutor}/{idCategoria}/{idStatus}/{idUserPublish}/{idEditorial}/{descargas}")
async def create_upload_file(  titulo:str,idAutor:str,idCategoria:int,idStatus:int,idUserPublish:str,idEditorial:str
                               ,descargas:int, archivo: UploadFile = File(...)) -> LibrosEntity:
        print(idUserPublish)
        Libro = LibrosEntity(id="S" ,titulo= str(titulo),idAutor=str(idAutor),idCategoria=int(idCategoria),idStatus= int(idStatus),fPublicacion="klk",idUserPublish=str(idUserPublish),idEditorial=str(idEditorial),descargas = int(descargas),archivoNombre= str(archivo.filename))

        with open(f"{paths.libros()}{archivo.filename}","wb") as myFile:
            content = await  archivo.read()
            myFile.write(content)
            myFile.close()
        trigger = core.crearLibro(Libro)
        if trigger['status'] == True:
            return trigger['response']
        else:
            raise HTTPException(400, trigger['mesagge'])


@Libros.get("/getAll")
async def getAllLibros()-> list[LibrosEntity]:
    trigger = core.getAllLibros()

    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])