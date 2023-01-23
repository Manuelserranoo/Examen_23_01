def ordenar_versos(verso):
    # Crear un diccionario con las líneas del verso y su posición correcta
    poema = {
        "El día 12 de Navidad mi verdadero amor me dio": 1,
        "12 bateristas tocando el tambor": 2,
        "11 tubería de gaiteros": 3,
        "10 señores un salto": 4,
        "9 damas bailando": 5,
        "8 criadas un ordeño": 6,
        "7 cisnes nadando": 7,
        "6 gansos una puesta": 8,
        "5 anillos de oro": 9,
        "4 pájaros cantando": 10,
        "3 gallinas francesas": 11,
        "2 tórtolas y": 12,
        "1 perdiz en un peral": 13
    }
    
    ordenado = sorted(verso, key=lambda x: poema[x])
    
    return ordenado
if __name__=="__main__":
    desordenado = [ "2 tórtolas y","11 tubería de gaiteros","12 bateristas tocando el tambor", "8 criadas un ordeño","5 anillos de oro", "10 señores un salto","7 cisnes nadando","3 gallinas francesas", "El día 12 de Navidad mi verdadero amor me dio","1 perdiz en un peral", "6 gansos una puesta", "4 pájaros cantando","9 damas bailando"]
    ordenado = ordenar_versos(desordenado)
    print(ordenado)

