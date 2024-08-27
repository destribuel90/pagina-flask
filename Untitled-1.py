class pedro():
    def __init__(self,variable1=None,variable3=None):
        self._variable1 = variable1
        self.__variable2=None
        self.variable3 = variable3

    def getVariable2(self):
        return self.__variable2
    def setVariable2(self,variable2):
        self.__variable2=variable2
    def clase(self):
        print("hola")
clasesita = pedro()
clasesita.clase()
