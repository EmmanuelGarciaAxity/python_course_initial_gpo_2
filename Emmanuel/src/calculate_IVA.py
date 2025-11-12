
'''
    Agegar iva a los productos
'''
products: list[float] = [100, 200, 300, 400, 500]

def add_IVA_to_product(price: float) -> float:
    ''' Funcion para agregar iva a un producto'''
    return price * 0.16 + price

def add_IVA_to_products(products: list[float]) -> list[float]:
    ''' Funcion para agregar iva a una lista de productos'''
    return list(map(add_IVA_to_product, products))



print("Forma mas compleja")

print(add_IVA_to_products(products))


'''
    Agregar iva de forma mas simple
'''
print("Forma mas simple")
print(list(map(lambda price: price * 0.16 + price, products)))
