from typing import Annotated
from fastapi import FastAPI,Depends
import uvicorn
from uvicorn import Config
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from Router.Categoria.CategoriaRouter import CATEGORIAS
"""
from Router.Clientes.ClientesRouter import CLIENTES


from Router.POS.POSRouter import POS
from Router.Pagos.PagosRouter import PAGOS
from Router.user.userRouter import USER
from Router.Pagos.conceptosRouter import CONCEPTOS
from Router.Finance.financeRouter import FINANCE
from Router.Ordenes.ordenesRouter import ORDENES
from Router.Productos.ProductosRouter import PRODUCTOS
from Router.Ordenes.pedidosRouter import PEDIDOS
"""
origins = ["*"]
app =FastAPI(title="crisostomo ",version="1.0",openapi_url="/localhost",logger="info")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/Padel/test")
async def test():
    return True
"""app.include_router(POS)
app.include_router(PAGOS)
app.include_router(PRODUCTOS)
app.include_router(ORDENES)
app.include_router(USER)
app.include_router(CLIENTES)
app.include_router(FINANCE)
app.include_router(CONCEPTOS)
app.include_router(PEDIDOS)"""
app.include_router(CATEGORIAS)
if __name__ == '__main__':
    configServer: Config = uvicorn.Config("main:app",port=8010,reload=True,log_level="info",host="0.0.0.0")
    server = uvicorn.Server(configServer)
    server.run()