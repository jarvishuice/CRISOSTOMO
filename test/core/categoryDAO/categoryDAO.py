from core.Implements.category.categoryDAO import CategoryDAO,CategoryEntity

class CategoryDAOTest(CategoryDAO):
    def __init__(self):
        super().__init__()
    def testCountId(self):
        a=self.countID()
        print(a['response'])
    def testCrearCategori(self,param:CategoryEntity):
        resultado =self.crearCategria(param)
        print(str(resultado))



test = CategoryDAOTest()
test.testCountId()
test.testCrearCategori(CategoryEntity(id=int(10),nombre=" test"))