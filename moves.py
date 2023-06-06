import random
x = random.randint(1,3)

def end_fight():
    atk = sword
    defe = armor
    playr = player('Player', '20', '2')
    end = enderman('Endermen', '26', '6', '6')
    x = random.randint(1,3)
    while end.ehp > 0:
        move = input("What move do you want to do? (Ex. atk, defe, heal)  ")
        if move == "atk":
            print("X IS:")
            print(int(x))
            if int(x) == 1:
                atk = atk - end.edefe
                end.ehp = end.ehp - atk
                print('Enderman has defended itself.')
                print("Enderman hp is now:")
                print(end.ehp)
                end.edefe = 6
                atk = sword
                x = random.randint(1,3)
            elif int(x) == 2 or 3:
                end.ehp = end.ehp - atk
                print("Enderman hp is")
                print(end.ehp)
                playr.hp = playr.hp - end.eatk
                print('Enderman has hit you')
                print('Your hp is now:')
                print(playr.hp)
                end.eatk = 6
                atk = sword
                x = random.randint(1,3)
            if playr.hp <= 0:
                print('l bozo. u died')
                break
        elif move == "heal":
            print("X IS:")
            print(int(x))
            playr.hp = playr.hp + playr.heal
            print("You have healed. Your hp is now:")
            print(playr.hp)
            if int(x) == 1:
                print('Enderman has defended itself.')
                print("Enderman hp is now:")
                print(end.ehp)
                end.edefe = 6
                x = random.randint(1,3)
            elif int(x) == 2 or 3:
                playr.hp = playr.hp - end.eatk
                print('Enderman has hit you')
                print('Your hp is now:')
                print(playr.hp)
                eatk = 6
                x = random.randint(1,3)
            if playr.hp <= 0:
                print('l bozo. u died')
                break
        elif move == "defe":
                print("X IS:")
                print(int(x))
                if int(x) == 2 or 3:
                    end.eatk = end.eatk - defe
                    playr.hp = playr.hp - eatk 
                    if playr.hp > 20:
                        playr.hp = 20
                        print('Enderman has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(playr.hp)
                        end.eatk = 6
                    else:
                        print('Enderman has hit you')
                        print('You defended yourself')
                        print('Your hp is now:')
                        print(playr.hp)
                        end.eatk = 6
                        x = random.randint(1,3)
                if int(x) == 1:
                    print('Both of you defended. No hp changes.')
                    x = random.randint(1,3)
                if playr.hp <= 0:
                    print('l bozo. u died')
                    break


def zomb_fight():
   atk = sword
   defe = armor
   zomb = zombie('Zombie', '16', '4', '5')
   playr = player('Player', '20', '2')
   x = random.randint(1,3)
   while zomb.ehp > 0:
       move = input('What move do you want to do? (Ex. atk, defe, heal) ')
       if move == "atk":
               print("X IS:")
               print(int(x))
               if int(x) == 1:
                   atk = atk - zomb.edefe
                   if atk <= 0:
                       print('Zombie has blocked your attack.')
                       print("Zombie hp is now:")
                       print(zomb.ehp)
                       zomb.edefe = 5
                       atk = sword
                       x = random.randint(1,3)
                   else:
                       zomb.ehp = zomb.ehp - atk
                       print('Zombie has blocked your attack.')
                       print("Zombie hp is now:")
                       print(zomb.ehp)
                       zomb.edefe = 5
                       atk = sword
                       x = random.randint(1,3)
               elif int(x) == 2 or 3:
                   zomb.ehp = zomb.ehp - atk
                   print("You have attacked the Zombie. Zombie hp is:")
                   print(zomb.ehp)
                   playr.hp = playr.hp - zomb.eatk
                   print('Zombie has hit you')
                   print('Your hp is now:')
                   print(playr.hp)
                   zomb.eatk = 4
                   atk = sword
                   x = random.randint(1,3)
       if move == "heal":
               print("X IS:")
               print(int(x))
               playr.hp = playr.hp + playr.heal
               if playr.hp > 20:
                   playr.hp = 20
                   print("You have healed. Your hp is now:")
                   print(playr.hp)
                   if int(x) == 1:
                       print('Zombie has defended itself.')
                       print("Zombie hp is now:")
                       print(zomb.ehp)
                       zomb.edefe = 5
                   elif int(x) == 2 or 3:
                       playr.hp = playr.hp - zomb.eatk
                       print('Zombie has hit you')
                       print('Your hp is now:')
                       print(playr.hp)
                       zomb.eatk = 4
                   x = random.randint(1,3)
               else:
                   print("You have healed. Your hp is now:")
                   print(playr.hp)
                   if int(x) == 1:
                       print('Zombie has defended itself.')
                       print("Zombie hp is now:")
                       print(zomb.ehp)
                       zomb.edefe = 5
                   elif int(x) == 2 or 3:
                       playr.hp = playr.hp - zomb.eatk
                       print('Zombie has hit you')
                       print('Your hp is now:')
                       print(playr.hp)
                       zomb.eatk = 4
                   x = random.randint(1,3)
       if move == "defe":
               print("X IS:")
               print(int(x))
               if int(x) == 1:
                   print('Both of you had defended. No hp changes.')
                   zomb.edefe = 5
               elif int(x) == 2 or 3:
                   zomb.eatk = zomb.eatk - defe
                   if zomb.eatk <= 0:
                       print("You have blocked the zombie's attack. You have lost no health.")
                       zomb.eatk = 4
                   elif zomb.eatk >= 1:
                       playr.hp = playr.hp - zomb.eatk
                       print('Zombie has hit you')
                       print('You defended yourself')
                       print('Your hp is now:')
                       print(playr.hp)
                       zomb.eatk = 4
               x = random.randint(1,3)
   if playr.hp <= 0:
        print('l bozo. u died')
  


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


class mob:
   def __init__(self, name):
       self.name = name
class player(mob):
    def __init__(self, name, hp, heal):
        super().__init__(name)
        self.hp = int(hp)
        self.heal = int(heal)
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.heal}"
class zombie(mob):
   def __init__(self, name, ehp, eatk, edefe):
       super().__init__(name)
       self.ehp = int(ehp)
       self.eatk = int(eatk)
       self.edefe = int(edefe)
   def __str__(self):
       return f"{self.name}, {self.ehp}, {self.eatk}, {self.edefe}"
class enderman(zombie):
   def __init__(self, name, ehp, eatk, edefe):
       super().__init__(name, ehp, eatk, edefe)
   def __str__(self):
       return f"{self.name}, {self.ehp}, {self.eatk}, {self.edefe}"
class ravager(zombie):
   def __init__(self, name, ehp, eatk, edefe):
       super().__init__(name, ehp, eatk, edefe)
   def __str__(self):
       return f"{self.name}, {self.ehp}, {self.eatk}, {self.edefe}"

playr = player('Player', '20', '2')
zomb = zombie('Zombie', '16', '4', '5')
end = enderman('Endermen', '26', '6', '6')
rav = ravager('Ravager', '32', '10', '8')

fight = input('Do you want to fight? (Ex. Y or N) ')
if fight == "Y":
    if playr.hp > 0:
        print("You are fighting the zombie. Like its basically impossible to die here, just don't be bad.")
        if zomb.ehp >= 0:
            zomb_fight()
        if zomb.ehp <= 0:
            print("The zombie has been slain.")
            print("You are now fighting the enderman. Getting harder.")
        if end.ehp >= 0:
            end_fight()
        if end.ehp <= 0:
            print("The enderman has been defeated.")
            print("Your fighting the ravager, gl my guy.")
        if rav.ehp >= 0:
            rav_fight()
    if playr.hp <= 0:
        print("You have died. El bozo. Get better.")

