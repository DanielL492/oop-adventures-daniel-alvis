import random
from fight import zomb_fight, end_fight, rav_fight
from classes import player, zombie, enderman, ravager

s = random.randint(1,1000)
if int(s) >= (1) and int(s) <= (400):
    sword = 4
    print("You got a wooden sword! 40%")
elif int(s) >= (501) and int(s) <= (550):
    sword = 1
    print("You got your fist..... SHELL POZO 5%")
elif int(s) >= (551) and int(s) <= (750):
    sword = 5
    print("You got a stone sword! 20%")
elif int(s) >= (401) and int(s) <= (500):
    sword = 7
    print("You got a diamond sword! 10%")
elif int(s) >= (751) and int(s) <= (800):
    sword = 9
    print("You got a netherite sword! 5%")
elif int(s) >= (801) and int(s) <= (999):
    sword = 6
    print("You got a iron sword! 19.9%")
elif int(s) == 1000:
    sword = 69420
    print("Bro got the UNFRIGGINBELIEVALIST. Use it wisely. 0.1%")
atk = sword
print(atk)

y = random.randint(1,1000)
if int(y) >= (1) and int(y) <= (200):
    armor = 3
    print("You got Leather Armor 20%")
if int(y) >= (651) and int(y) <= (800):
    armor = 4
    print("You got Gold Armor 15%")
elif int(y) >= (201) and int(y) <= (350):
    armor = 5
    print("You got Chainmail Armor 15%")
elif int(y) >= (351) and int(y) <= (500):
    armor = 6
    print("You got Iron Armor 15%")
elif int(y) >= (501) and int(y) <= (600):
    armor = 8
    print("You got Diamond Armor 10%")
elif int(y) >= (601) and int(y) <= (650):
    armor = 9
    print("You got Netherite Armor 5%")
elif int(y) >= (801) and int(y) <= (900):
    armor = 1
    print("No Armor...... SHELL POZO 10%")
elif int(y) >= (901) and int(y) <= (999):
    armor = 7
    print("You got Emerald...Armor? 9.9%")
elif int(y) == (1000):
    armor = 263319020
    print("You have obtained ShellPozer (Superior) (Spartan) Armor.... Use it wisely 0.1%")
defe = armor
print(defe)


playr = player('player', '20', '2')
zomb = zombie('Zombie', '16', '4', '5')
end = enderman('Endermen', '26', '6', '6')
rav = ravager('Ravager', '32', '10', '8')


fight = input('Do you want to fight? (Ex. Y or N) ')
while fight == "Y":
    if playr.hp > 0:
        print("You are fighting the zombie. Like its basically impossible to die here, just don't be bad.")
        if zomb.ehp > 0:
            zomb_fight()
        elif playr.hp <= 0:
            print("L bozo. U died")
        if end.ehp > 0:
            end_fight()
        elif playr.hp <= 0:
            print("L bozo. U died")
            break
        if rav.ehp > 0:
            rav_fight()
        elif playr.hp <= 0:
            print("L bozo. U died")