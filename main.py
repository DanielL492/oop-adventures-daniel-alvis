from fightanditems import zomb_fight, end_fight, rav_fight
from classes import player, zombie, enderman, ravager

playr = player('player', '20', '4')
zomb = zombie('Zombie', '16', '4', '5')
end = enderman('Endermen', '26', '6', '6')
rav = ravager('Ravager', '32', '9', '6')


fight = input('Do you want to fight? (Ex. y or n) ')
if fight == "y":
    if playr.hp > 0:
        print("You are fighting the zombie. Like its basically impossible to die here, just don't be bad.")
        if zomb.ehp > 0:
            zomb_fight()
            if end.ehp > 0:
                end_fight()
                if rav.ehp > 0:
                    rav_fight()
            elif playr.hp <= 0:
                print("L bozo. U died")