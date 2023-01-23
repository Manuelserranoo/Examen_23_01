class operar():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def exponencial(self):
        if self.num2 < 0:
            return "nil"
        e = num1**num2
        return e

if __name__=="__main__":
    num1 = int(input("Introduce el índice:"))
    num2 = int(input("Introduce el exponente:"))
    a = operar(num1,num2)
    print(a.exponencial())
