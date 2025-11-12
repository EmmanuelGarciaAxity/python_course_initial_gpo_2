class CustomError(Exception):
    ''' Error personalizado '''
    pass

def function_con_error(n1: int):
    if n1 < 0:
        raise CustomError("El numero debe ser mayor a 0")
    return n1

try:
    function_con_error(-1)
except Exception as e :
    print(f"Error: {e}")
else:
    print(f"Resultado correcto")

finally:
    print("Fin del programa")
