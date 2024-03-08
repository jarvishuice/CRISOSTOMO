from Core.Entities.Categorias.SubCategoriaEntity import SubCategoriaEntity
from Core.Implements.Categoria.CategoriaDAO import CategoriasEntity,CategoriasDAO,Logs,ResponseInternalEntity

class CategoriasServices(Logs):
    __Core = CategoriasDAO()
    def __init__(self):
        super().__init__()
    @property
    def LeerCategorias(self) -> list[CategoriasEntity] | ResponseInternalEntity :
        return self.__Core.getAllCategoria
    def BuscaraCategoriaById(self,id:int)-> list[CategoriasEntity]|ResponseInternalEntity:
        return self.__Core.searchCategoriaById(id=id)
    @property
    def LeerSubCategorias(self) ->  list [SubCategoriaEntity] | ResponseInternalEntity:
        return self.__Core.getAllSubCategorias
    def BuscarSubCategoriaByCategoria(self,id:int) -> list[SubCategoriaEntity] | ResponseInternalEntity:
        return self.__Core.getSubCategoriaByCategoria(id)