# Escribe una función que reciba una lista de string y nos retorne el que tiene menos caracteres.
def mas_corta(palabras):
    pos = 0
    for x in range(len(palabras)):
        if len(palabras[x]) < len(palabras[pos]):
            pos = x
    return palabras[pos]

# Bloque principal 
palabras = ["Ana", "Carlos", "Beatriz", "Juan", "Pedro", "Sofia"]
print("palabras con menos caracteres:", mas_corta(palabras))
