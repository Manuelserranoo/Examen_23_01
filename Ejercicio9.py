class Warrior:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.block = None
        self.deceased = False
        self.zombie = False
    
    def attack(self, defender, attack_position):
        if self.deceased or defender.deceased:
            return
        if defender.block == attack_position:
            return
        if attack_position == Position.high:
            damage = 10
        elif attack_position == Position.low:
            damage = 5
        else:
            damage = 0
        if defender.block is None:
            damage += 5
        defender.vida -= damage
        if defender.vida <= 0:
            defender.deceased = True
            defender.zombie = True

class Position:
    high = 'high'
    low = 'low'


if __name__=="__main__":
    warrior1 = Warrior("warrior1")
    warrior2 = Warrior("warrior2")
    warrior1.attack(warrior2, Position.high)
    print(warrior2.vida)
    warrior1.attack(warrior2, Position.low)
    print(warrior2.vida)