def sumar(lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return suma

# Bloque principal
mi_lista = [1, 2, 3]
print("suma:", sumar(mi_lista))
print("Original:", mi_lista)
