# Definición de la función con parámetros predeterminados 
def calcular_descuento(precio, descuento=0.10):
    return precio - (precio * descuento)

# Llamdas a la función
print(calcular_descuento(100))             # Usa el descuento predeterminado del 10%
print(calcular_descuento(100, 0.20))       # Usa un descuento del 20%