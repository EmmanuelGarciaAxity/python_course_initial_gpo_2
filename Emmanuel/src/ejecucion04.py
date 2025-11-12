import time

'''
    Decoradores -> Aumenta funcionalidad de una funcion sin modificar su funcion original

'''




def decorar_saludo(func):
    def envoltura():
        print("Iniciando la funcion")
        func()
        print("Fin de la funcion")
    return envoltura


@decorar_saludo
def saludar():
    print("Hola, como estas?")
saludar()




# Decorador con args y kwargs

def decorar(func):
    def envoltura(*args, **kwargs):
        print("Iniciando con args {args} y kwargs {kwargs}")
        func(*args, **kwargs)
        print("Fin de la funcion")
    return envoltura

@decorar
def suma(num_1: int, num_2: int) -> None:
    print(f"La suma de {num_1} y {num_2} es {num_1 + num_2}")

suma(1, 2)




def decorador_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        fin = time.time()
        print(f"Tiempo de inicio: {inicio} y tiempo de fin: {fin}")
        print(f"Tiempo de fin: {fin - inicio} segundos")

        ejecucion = func(*args, **kwargs)
        
        print(f"Resultado de ejecucion: {ejecucion}")
    
        return ejecucion
    return envoltura

@decorador_tiempo
def funcion_que_tarda() -> None:
    time.sleep(1)
    print("Funcion que tarda 1 segundo")

funcion_que_tarda()



