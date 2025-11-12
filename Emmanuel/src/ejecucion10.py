from dataclasses import dataclass

@dataclass
class Motor:
    tipo:str

@dataclass
class Rueda:
    tamaño:int


@dataclass
class Coche:
    marca:str
    motor:Motor
    ruedas:list[Rueda]

    def __str__(self):
        return f"Coche marca {self.marca}, motor {self.motor.tipo}, ruedas {len(self.ruedas)}"


auto_uno = Coche(marca="Toyota", motor=Motor(tipo="Diesel"), ruedas=[Rueda(tamaño=16), Rueda(tamaño=16)])
print(auto_uno)

