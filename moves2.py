import random
x = random.randint(1, 3)
class mob:
    def __init__(self, name):
        self.name = name
class zombie(mob):
    def __init__(self, name, zhp, zatk, zdefe):
        super().__init__(name)
        self.zhp = zhp
        self.zatk = zatk
        self.zdefe = zdefe
    def __str__(self):
        return f"{self.zhp}, {self.zatk}, {self.zdefe}"
class enderman(mob):
    def __init__(self, name, ehp, eatk, edefe, eheal):
        super().__init__(name)
        self.ehp = ehp
        self.eatk = eatk
        self.edefe = edefe
        self.eheal = eheal
    def __str__(self):
        return f"{self.ehp}, {self.eatk}, {self.edefe}, {self.eheal}"
class ravager(mob):
    def __init__(self, name, rhp, ratk, rdefe, rheal):
        super().__init__(name)
        self.rhp = rhp
        self.ratk = ratk
        self.rdefe = rdefe
        self.rheal = rheal
    def __str__(self):
        return f"{self.rhp}, {self.ratk}, {self.rdefe}, {self.rheal}"
   
hp = 20
atk = 5
defe = 6
heal = 2


zhp = 15
zatk = 2
zdefe = 4


ehp = 25
eatk = 5
edefe = 5
eheal = 1


rhp = 30
ratk = 8
rdefe = 6
rheal = 2
while hp >= 0:
    fight = input('Do you want to fight? ')
    if fight == "yes":
        while zhp >= 0:
            print('You are fighting the zombie')
            move = input('What move do you want to do? (Ex. attack, defend, heal) ')
            if move == "attack":
                zhp = zhp - atk
                atk = 4
                print("Zombie hp is")
                print(zhp)
            elif move == "heal":
                hp = hp + heal
                print("You have healed. Your hp is now:")
                print(hp)
            if int(x) == 1:
                hp = hp - zatk
                print('Zombie has hit you')
                print('Your hp is now:') 
                print(hp)
            if int(x) == 2:
                hp = hp - zatk
                print('Zombie has hit you')
                print('Your hp is now:')
                print(hp)
            if int(x) == 3:
                atk = atk - zdefe
                print('Zombie has defended itself')
