#Crearemos una funciona que haga el cifrado de vigeneré con respecto al de cesar

def cifrado(cadena,key):
    cadena = cadena.lower()
    key = key.lower()
    cifrado = ""
    for i in range(len(cadena)):
        cifrado += chr((ord(cadena[i]) + ord(key[i%len(key)]) - 2*ord('a'))%26 + ord('a'))
    return cifrado

def descifrado(cadena,key):
    cadena = cadena.lower()
    key = key.lower()
    descifrado = ""
    for i in range(len(cadena)):
        descifrado += chr((ord(cadena[i]) - ord(key[i%len(key)]) + 26)%26 + ord("a"))
    return descifrado

if __name__=="__main__":
    cadena = "HELLOWORLD"
    key = "ABCXYZ"
    print(cifrado(cadena,key))
    print(descifrado(cifrado(cadena,key),key))