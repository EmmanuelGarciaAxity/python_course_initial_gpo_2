#Comentario en linea


"""
Comentario en bloque
"""

#Tipo de datos

nombre = "Juan"
print(type(nombre))
edad = 20
print(type(edad))
altura = 1.75
print(type(altura))

#Listas

mi_lista = [1, 2, 3, 4, 5]
print("Mi lista antes de modificar: ", mi_lista)

#mi_lista[2] = 4 # Modificar el valor de la lista

print("Mi lista despues de modificar: ", mi_lista)

mi_diccionario = {"nombre": "Juan", "edad": 20, "altura": 1.75}
print("Mi diccionario antes de modificar: ", mi_diccionario)

mi_set = {1, 2, 3, 4, 5}
print("Mi set antes de modificar: ", mi_set)


#f-stirng

nombre: str = "Juan"

print("Mi nombre es: "+ nombre)
print(f"Mi nombre es {nombre}")


"""
Compresiones
"""	
cuadrados: list = [x**2 for x in range(10)]

print(cuadrados)


#break, continue, else en bucles

def saludar(nombre: str) -> void:
    ''' Funcion para saludar'''
    print(f"Hola, {nombre}")

saludar("Juan")

