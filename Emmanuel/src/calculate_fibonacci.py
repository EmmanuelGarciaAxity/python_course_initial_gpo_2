'''
    Calcular la secuencia de Fibonacci
'''

def calculate_fibonacci(n: int) -> int:
    ''' Funcion para calcular la secuencia de Fibonacci'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        anterior = 0
        actual = 1
        print(f"Fibonacci #{0}: {anterior}")
        print(f"Fibonacci #{1}: {actual}")
        for posicion in range(2, n):
            siguiente = anterior + actual
            anterior = actual
            actual = siguiente
            print(f"Fibonacci #{posicion}: {actual}")
        return actual

print(calculate_fibonacci(10))