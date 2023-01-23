#crear una funcion que juegue al texas holdem	

def texas_holdem(comunitarias):
    import random
    cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    palos = ["C","D","T","P"]
    for i in range(5):
        comunitarias.append(random.choice(cartas) + random.choice(palos))
    return comunitarias
#crear otra funcion que de dos artas aleatorias
def mano(manojugador):
    import random
    cartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    palos = ["C","D","T","P"]
    for i in range(2):
        manojugador.append(random.choice(cartas) + random.choice(palos))
    return manojugador
#crear una funcion que ordene las cartas por importancia
def ordenar(manojugador,comunitarias):
    manoconjunta = manojugador + comunitarias
    print(manoconjunta)
    for i in manoconjunta:
        if i[0] == "A":
            i = "14" + i[1]
        elif i[0] == "J":
            i = "11" + i[1]
        elif i[0] == "Q":
            i = "12" + i[1]
        elif i[0] == "K":
            i = "13" + i[1]
        manoconjunta.sort()
        #devolver las 5 mejores cartas
    return manoconjunta
    

if __name__ == "__main__":
    manojugador = []
    comunitarias = []
    print(texas_holdem(comunitarias))
    print(mano(manojugador))
    print(ordenar(manojugador,comunitarias))
