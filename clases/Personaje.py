class Personaje:
    #constructor
    def __init__(self):
        #atributos
        self.__nombre=None 
        self.__edad=None

    #metodos get, obtener el valor de un atributo
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

#metodos set (escribr/ingresas/llevar un valor a un atributo)
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @edad.setter
    def edad(self,edad):
        if(edad<0):
            print("No acepto edades negativas")
        else:
            self.__edad=edad

    