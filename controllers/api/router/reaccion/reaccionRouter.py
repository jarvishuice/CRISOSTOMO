
from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.reaccion.reaccionDAO import ReaccionDAO,ReaccionEntity,ReaccionDetailEntity
##probando el git

core = ReaccionDAO()
#security = HTTPBearer()
#validator = AuthDAO()
urlBase = "/crisostomo/"
Reaccion = APIRouter(prefix=f"{urlBase}Reaccion", tags=["Reaccion"])


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


@Reaccion.post("/")
async def crearReaccion (React: ReaccionEntity) -> ReaccionEntity:
    datos =React
    trigger = core.crearReaccion(datos)
    print("pase"+id())
    if trigger['status'] == True:
        respuesta = trigger['response']
        return respuesta
    else:
        raise HTTPException(400, trigger['mesagge'])
@Reaccion.get("/getAll")
async def getAllReaction () -> list[ReaccionDetailEntity]| object:

    trigger = core.getAllReaccion()

    if trigger['status'] == True:
        respuesta = trigger['response']
        return respuesta
    else:
        raise HTTPException(400, trigger['mesagge'])
@Reaccion.get("/filter/Libro/{idLibro}")
async def retReaccionByLibro(idLibro:str) -> list[ReaccionDetailEntity]:
    trigger = core.filterReaccionByLibro(idLibro)
    if trigger['status'] == True:
        respuesta = trigger['response']
        return respuesta
    else:
        raise HTTPException(400, trigger['mesagge'])