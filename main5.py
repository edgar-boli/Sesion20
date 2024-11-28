def mayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

# Bloque principal
numeros = [12, 45, 7, 23, 89, 34]
print("Mayor:", mayor(numeros))
