def power_of_4(n):
    #devolver falso si no es un entero
    if not isinstance(n, int):
        return False
    #devolver falso si es negativo
    elif n <= 0:
        return False
    while n > 1:
        if n % 4 != 0:
            return False
        n = n // 4
    return True


if __name__ == "__main__":
    print(power_of_4(1024))
    print(power_of_4(55))
    print(power_of_4("Four"))
    print(power_of_4(4096))
    print(power_of_4(0))


    
