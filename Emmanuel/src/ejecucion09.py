'''
Modelado de objectos mediante composición y herencia

'''

class Motor:
        def __init__(self, tipo:str):
            self.tipo = tipo

class Rueda:
    def __init__(self, tamaño:int):
        self.tamaño = tamaño

class Coche:
    def __init__(self,marca:str, motor:Motor, rueda:list[Rueda]):
        self.marca = marca
        self.motor = motor
        self.rueda = rueda

    def descripcion(self):
        print(f"Coche marca {self.marca}")
        print(f"Tipo de motor {self.motor.tipo}")
        for i, rueda in enumerate(self.rueda, 1):
            print(f"Tamaño de la rueda {i}: {rueda.tamaño}")


auto_uno = Coche(
    marca="Toyota",
    motor=Motor("Diesel"),
    rueda= [Rueda(2),Rueda(2)]
)

auto_uno.descripcion()