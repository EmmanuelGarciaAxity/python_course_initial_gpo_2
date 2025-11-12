class Producto:
    ''' Clase Producto '''
    def __init__(self, nombre:str):
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre:str) -> None:
        ''' Setter del nombre '''
        if len(nuevo_nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        self._nombre = nuevo_nombre

producto = Producto("Laptop")

print(producto.nombre)

producto.nombre = "L"

print(producto.nombre)