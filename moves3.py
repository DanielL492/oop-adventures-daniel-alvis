
import random
s = random.randint(1,1000)
def sword():
    if int(s) >= (1) and int(s) <= (400):
        atk = 4
        print("You got a wooden sword! 40%")
    elif int(s) >= (501) and int(s) <= (550):
        atk = 1
        print("You got your fist..... SHELL POZO 5%")
    elif int(s) >= (551) and int(s) <= (750):
        atk = 5
        print("You got a stone sword! 20%")
    elif int(s) >= (401) and int(s) <= (500):
        atk = 7
        print("You got a diamond sword! 10%")
    elif int(s) >= (751) and int(s) <= (800):
        atk = 9
        print("You got a netherite sword! 5%")
    elif int(s) >= (801) and int(s) <= (999):
        atk = 6
        print("You got a iron sword! 19.9%")
    elif int(s) == 1000:
        atk = 69420
        print("Bro got the UNFRIGGINBELIEVALIST. Use it wisely. 0.1%")
sword()
y = random.randint(1,1000)





