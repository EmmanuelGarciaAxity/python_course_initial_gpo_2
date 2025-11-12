'''
Herencia y composición
'''


class Animal:
    ''' Clase Animal '''
    def __init__(self, nombre:str = "Firulais"):
        self.nombre = nombre
    def hablar(self):
        print("El animal habla")


class Perro(Animal):
    ''' Clase Perro '''
    def __init__(self, nombre:str = "Firulais",raza:str = "Labrador"):
        super().__init__(nombre)
        self.raza = raza
    def hablar(self):
        print(self.nombre)
        print("guau guau")

animal = Animal()
perro = Perro()

animal.hablar()

perro.hablar()