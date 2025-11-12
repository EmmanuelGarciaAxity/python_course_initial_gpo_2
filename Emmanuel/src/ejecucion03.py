'''
    Args y kwargs
'''


def procesar_datos(*args):

    print(f"Los argumentos son: {args}")

procesar_datos(2, 3, 4)




def saludos_dinamicos(**kwargs) -> None:

    print(f"Los argumentos son: {kwargs}")


saludos_dinamicos(nombre="Juan", edad=20)


#Generadores -> Para manejar grandes volumenes de datos, utilizan yield en lugar de return

def generar_datos(limite: int):
    '''Generador que produce numeros hasta un limite dado'''
    print("Inicio del generador")
    for num in range(limite):
        print(f"Bucle en posicion: {num}")
        yield num
    print("Fin del generador")

def generar_datos_tradicional(limite: int):
    '''Generador que produce numeros hasta un limite dado'''
    print("Inicio del generador")
    resultado = []
    for num in range(limite):
        print(f"Bucle en posicion: {num}")
        resultado.append(num)
    print("Fin del generador tradicional")
    return resultado


print("Uso del generador")

generador = generar_datos(5)


for numero in generador:
    print(f"Numero: {numero}")


print("Uso del generador tradicional")
lista = generar_datos_tradicional(5)

for item in lista:
    print(f"Item: {item}")  