
from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Response, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.Implements.category.categoryDAO import CategoryDAO,CategoryEntity


core = CategoryDAO()
#security = HTTPBearer()
#validator = AuthDAO()
urlBase = "/crisostomo/"
Categoria = APIRouter(prefix=f"{urlBase}Categorias", tags=["Categorias"])


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


@Categoria.post("/")
async def crearCategoria (category:CategoryEntity)-> CategoryEntity :
    datos =category
    trigger = core.crearCategria(datos)

    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])
@Categoria.get("/getAll")
async def getAllCategory()-> list[CategoryEntity]:
    trigger = core.getAllCategory()

    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])
@Categoria.get("/count")
async def contarCategorias():
    trigger = core.countID()

    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])
@Categoria.get("/search/{nombre}")
async def busquedaCategoria(nombre:str):
    trigger = core.searchCategoryByName(nombre)
    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])