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