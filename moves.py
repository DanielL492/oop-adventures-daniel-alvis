import random
guess = input("guess")
x = random.randint(1, 3)
if int(guess) == 

hp = 20
atk = 4
defe = 6
heal = 3

attack = 1
defend = 2
heal = 3

zhp = 20
zatk = 1
zdefe = 2
zheal = 3

ehp = 25 
eatk = 1
edefe = 2
eheal = 3

rhp = 30
ratk = 1
rdefe = 2
rheal = 3

move = input('What move do you want to do? (Ex. attack, defend, heal) ')
if move == "attack":
    zhp = zhp - attack
    print("Zombie hp is")
    print(zhp)
elif move == "heal":
    hp = hp + heal
    print(hp)
else:
    