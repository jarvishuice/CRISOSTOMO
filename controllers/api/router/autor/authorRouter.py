
from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Response
from core.Implements.autor.autorDAO import AutorDAO,AutorEntity

core = AutorDAO()

urlBase = "/crisostomo/"
Autor = APIRouter(prefix=f"{urlBase}Autor", tags=["Autor"])


@Autor.post("/")
async def regAutor (autor: AutorEntity) :
    trigger = core.crearAutor(autor)

    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])
@Autor.get("/getAll")
async  def getAllAutor():
    trigger = core.getAllAutores()
    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])
@Autor.get("/search/{name}")
async def searchAutorByName(name:str)->list[AutorEntity]:
    trigger = core.searchAutoresByName(name)
    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])
@Autor.put("/actualizar/Cantidad/Libros/{idAutor}")
async def acuralizarNLibros(idAutor:str)->bool:
    trigger = core.ActualizarCantidadLibros(idAutor)
    if trigger['status'] == True :
        respuesta = trigger['response']
        return respuesta
    else :
        raise HTTPException(400, trigger['mesagge'])