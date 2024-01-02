from config.Logs.LogsActivity import Logs


class TestLogs(Logs) :
    def __init__ (self) -> object :
        pass

    def pruebaError (self) :
        print("Prueba Logs Error")
        x = self.Error("prueba error")
        if x == False :
            print("True")
        else :
            print("False")

    def pruebaWarining (self) :
        print("Prueba Logs Warning ")
        x = self.Warnings("prueba error")
        if x :
            print("True")
        else :
            print("False")

    def pruebaWiterTask (self) :
        x = self.Error("prueba error")
        if x :
            print("True")
        else :
            print("False")

    def testClassComplete (self) :
        self.pruebaError()
        self.pruebaWarining()


if __name__ == '__main__' :
    j = TestLogs()
    j.testClassComplete()
