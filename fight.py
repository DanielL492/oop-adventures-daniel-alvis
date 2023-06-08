fight = input('Do you want to fight? (Ex. Y or N) ')
if fight == "Y":
    if playr.hp > 0:
        print("You are fighting the zombie. Like its basically impossible to die here, just don't be bad.")
        if zomb.ehp > 0:
            zomb_fight()
            if zomb.ehp <= 0:
                    end_fight()
                    if end.ehp <= 0:
                        rav_fight()
