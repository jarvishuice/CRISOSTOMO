
from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.libros.librosDAO import LibrosDAO,LibrosEntity,Logs


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


@Libros.post("/")
async def crearLibro (Libro: LibrosEntity)->LibrosEntity :
    datos =Libro
    trigger = core.crearLibro(datos)

    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])
@Libros.get("/getAll")
async def getAllLibros()-> list[LibrosEntity]:
    trigger = core.getAllLibros()

    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])