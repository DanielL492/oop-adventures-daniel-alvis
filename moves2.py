class mob:
    def __init__(self, name):
        self.name = name
class zombie(mob):
    def __init__(self, name, hp, atk, defe, heal):
        super().__init__(name)
        self.hp = hp
        self.atk = atk 
        self.defe = defe
        self.heal = heal
class enderman(mob):
     def __init__(self, name, ehp, eatk, edefe, eheal):
        super().__init__(name)
        self.ehp = ehp
        self.eatk = eatk
        self.edefe = edefe
        self.eheal = eheal
class ravager(mob):
    def __init__(self, name, rhp, ratk, rdefe, rheal):
        super().__init__(name)
        self.rhp = rhp
        self.ratk = ratk 
        self.defe = rdefe
        self.rheal = rheal

import random
guess = input("guess")
x = random.randint(1, 3) 
hp = 20
atk = 4
defe = 6
heal = 3

attack = 1
defend = 2
heal = 3

zhp = 15
zatk = 2
zdefe = 4

ehp = 25 
eatk = 4
edefe = 5
eheal = 1

rhp = 30
ratk = 8
rdefe = 6
rheal = 2

move = input('What move do you want to do? (Ex. attack, defend, heal) ')
if move == "attack":
    zhp = zhp - attack
    print("Zombie hp is")
    print(zhp)
elif move == "heal":
    hp = hp + heal
    print(hp)
    