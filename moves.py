class move:
    def  __init__(self, name):
        self.name = name
class attk(move):
    def __init__(self, name, dmg):
        super().__init__(name)
        self.dmg = int(dmg)
    def __str__(self):
        return f"{self.name}, {self.dmg}"
class defend(move):
    def __init__(self, name, defe):
        super().__init__(name)
        self.defe = int(defe)
    def __str__(self):
        return f"{self.name},{self.defe}"
class heal(move):
    def __init__(self, name, hea):
        super().__init__(name)
        self.hea = int(hea)
    def __str__(self):
        return f"{self.name},{self.hea}"
    
claw = attk('claw','4')
swipe = attk('swipe','6')
ram = attk('ram', '10')

zdefend = defend('zdefend')