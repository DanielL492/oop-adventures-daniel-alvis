

import random
x = random.randint(1,3)


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


zhp = 16
zatk = 4
zdefe = 5


ehp = 26
eatk = 6
edefe = 6
eheal = 2


rhp = 32
ratk = 10
rdefe = 8
rheal = 4



while hp >= 0:
    fight = input('Do you want to fight? ')
    if fight == "yes":
        print('You are fighting the zombie')
        while zhp >= 0:
            move = input('What move do you want to do? (Ex. attack, defend, heal) ')
            if move == "attack":
                print("X IS:")
                print(int(x))
                if int(x) == 1:
                    atk = atk - zdefe
                    zhp = zhp - atk
                    print('Zombie has defended itself.')
                    print("Zombie hp is now:")
                    print(zhp)
                    zdefe = 5
                    atk = 5
                    x = random.randint(1,3)
                elif int(x) == 2 or 3:
                    zhp = zhp - atk
                    print("Zombie hp is")
                    print(zhp)
                    hp = hp - zatk
                    print('Zombie has hit you')
                    print('Your hp is now:')
                    print(hp)
                    zatk = 4
                    atk = 5
                    x = random.randint(1,3)
            elif move == "heal":
                print("X IS:")
                print(int(x))
                hp = hp + heal
                print("You have healed. Your hp is now:")
                print(hp)
                if int(x) == 1:
                    print('Zombie has defended itself.')
                    print("Zombie hp is now:")
                    print(zhp)
                    zdefe = 5
                    x = random.randint(1,3)
                elif int(x) == 2 or 3:
                    hp = hp - zatk
                    print('Zombie has hit you')
                    print('Your hp is now:')
                    print(hp)
                    zatk = 4
                    x = random.randint(1,3)
            elif move == "defend":
                print("X IS:")
                print(int(x))
                if int(x) == 2 or 3:
                    zatk = zatk - defe
                    hp = hp - zatk 
                    if hp > 20:
                        hp = 20
                        print('Zombie has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(hp)
                        zatk = 4
                    else:
                        print('Zombie has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(hp)
                        zatk = 4
                    x = random.randint(1,3)
                if int(x) == 1:
                    print('Zombie has defended itself.')
                    print("Zombie hp is now:")
                    print(zhp)
                    zdefe = 5
        print("The zombie has been slain.")

print("SHELLPOZO. Try again, or are you a pu-")

