import random
s = random.randint(1,1000)
def swor():
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
swor()

y = random.randint(1,20)
print(y)
def armor():
    if int(y) >= (1) and int(y) <= (4):
        armor = 4
        print("You got leather armor")
    elif int(y) >= (5) and int(y) <=(8):
        armor = 5
        print("You got chainmail armour")





