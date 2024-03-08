from fastapi import APIRouter, HTTPException
from services.Categorias.CategoriaServices import CategoriasEntity,CategoriasServices
core =CategoriasServices()
URL = '/crisostomo/categorias'
CATEGORIAS = APIRouter(prefix=URL, tags=[ "CATEGORIAS" ])
@CATEGORIAS.get("/get/all")
async def GetAllCategorias():
    trigger = core.LeerCategorias
    if trigger.status == False:
        raise HTTPException (400, trigger.message)
    return trigger.response
@CATEGORIAS.get("/get/{id}")
async def GetCategoriaById(id:int):
    trigger = core.BuscaraCategoriaById(id=id)
    if trigger.status == False:
        raise HTTPException (400, trigger.message)
    return trigger.response

@CATEGORIAS.get("/get/subcategoria/")
async def GetSubCategorias():
    trigger = core.LeerSubCategorias
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response
@CATEGORIAS.get("/get/subcategoria/{idCategoria}")
async def GetSubCategoriaByCategoria(idCategoria:int):
    trigger = core.BuscarSubCategoriaByCategoria(int(idCategoria))
    if trigger.status == False:
        raise HTTPException(400, trigger.message)
    return trigger.response