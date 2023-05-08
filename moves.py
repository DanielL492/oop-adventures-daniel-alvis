

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
    
print (zombie())

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

