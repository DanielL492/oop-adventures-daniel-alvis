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
class ad(zombie):
   def __init__(self, name, ehp, eatk, edefe):
       super().__init__(name, ehp, eatk, edefe)
   def __str__(self):
       return f"{self.name}, {self.ehp}, {self.eatk}, {self.edefe}"
class sword:
   def __init__(self, dmg):
       self.dmg = dmg
class pl(sword):
    def __init__(self, dmg):
        super().__init__(dmg)
    def __str__(self):
        return f"{self.dmg}"
class wood(pl):
    def __init__(self, dmg):
        super().__init__(dmg)
    def __str__(self):
        return f"{self.dmg}"
class stone(pl):
   def __init__(self, dmg):
       super().__init__(dmg)
   def __str__(self):
       return f"{self.dmg}"
class iron(pl):
   def __init__(self, dmg):
       super().__init__(dmg)
   def __str__(self):
       return f"{self.dmg}"
class diamond(pl):
   def __init__(self, dmg):
       super().__init__(dmg)
   def __str__(self):
       return f"{self.dmg}"
class netherite(pl):
   def __init__(self, dmg):
       super().__init__(dmg)
   def __str__(self):
       return f"{self.dmg}"
class fist(pl):
   def __init__(self, dmg):
       super().__init__(dmg)
   def __str__(self):
       return f"{self.dmg}"
class UNFRIGGINBELIAVALIST(pl):
   def __init__(self, dmg):
       super().__init__(dmg)
   def __str__(self):
       return f"{self.dmg}"
   
class mob:
   def __init__(self, name):
       self.name = name
class n(mob):
    def __init__(self, name, hp, heal):
        super().__init__(name)
        self.hp = int(hp)
        self.heal = int(heal)
    def __str__(self):
        return f"{self.name}, {self.hp}, {self.heal}"

fi = fist('1')
wo = wood('4')
st = fist('5')
ir = fist('6')
di = fist('7')
ne = fist('9')
un = fist('69420')

