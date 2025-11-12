def saludar(nombre: str = "Mundo") -> None:
    ''' Funcion para saludar'''
    print(f"Hola, {nombre}")



saludar("Juan")
saludar()


'''
Lambda functions
'''


sumar = lambda num_1, num_2: num_1 + num_2

resultado = sumar(1, 2)
print(f"El resultado de la suma es: {resultado}")


'''
    Maps
'''

lista = range(5)
operacion = lambda num_1: num_1 **2
resultado = map(operacion, lista)

print(list(resultado))


'''
    Filters
'''
print("Filtrar los numeros pares")
print(list(filter(lambda num_1: num_1 % 2 == 0, range(10))))
