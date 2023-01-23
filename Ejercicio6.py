import itertools

def palabras(cadena):
    posibilidades = list(itertools.permutations(cadena))

    posibilidades.sort()

    a = posibilidades.index(tuple(cadena))
    return a + 1



    
print(palabras("ABAB"))
print(palabras("AAAB"))
print(palabras("BAAA"))
print(palabras("PREGUNTA"))
print(palabras("CONTADOR"))