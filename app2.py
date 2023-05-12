import uuid

class sword:
    def __init__(self,swordsmaster):
        self.swordsmaster = swordsmaster

class silver_sword(sword):
    def __init__(self, swordsmaster, silver_sword, attack, silver_slash):
        super().__init__(swordsmaster, attack, silver_slash)
        self.silver_sword = silver_sword
        self.silver_slash = silver_slash
    def __str__(self):
        return f"{self.swordsmaster}, {self.silver_sword}, {self.silver_slash}"
class gold_sword(sword): 
    def __init__(self, swordsmaster, gold_sword, attack, gold_slash):
        super().__init__(swordsmaster, attack, gold_slash)
        self.gold_sword = gold_sword
        self.gold_slash = gold_slash
    def __str__(self):
        return f"{self.swordsmaster}, {self.gold_sword}, {self.gold_slash}"
class diamond_sword(sword):
    def __init__(self, swordsmaster, diamond_sword, attack, diamond_slash):
        super().__init__(swordsmaster, attack, diamond_slash)
        self.diamond_sword = diamond_sword
        self.diamond_slash = diamond_slash
    def __str__(self):
        return f"{self.swordsmaster}, {self.diamond_sword}, {self.diamond_slash}"

silver_slash = 10
gold_slash = 15
diamond_slash = 25




class staff:
    def __init__(self, mage):
        self.mage = mage

class silver_staff(staff):
    def __init__(self, mage, silver_staff):
        super().__init__(mage)
        self.silver_staff = silver_staff
    def __str__(self):
        return f"{self.mage}, {self.silver_staff}"
class gold_staff(staff):
    def __init__(self, mage, gold_staff):
        super().__init__(mage)
        self.gold_staff = gold_staff
    def __str__(self):
        return f"{self.mage}, {self.gold_staff}"
class diamond_staff(staff):
    def __init__(self, mage, diamond_staff):
        super().__init__(mage)
        self.diamond_staff = diamond_staff
    def __str__(self):
        return f"{self.mage}, {self.diamond_staff}"
    



class axe:
    def __init__(self, beserker):
        self.beserker = beserker

class silver_axe(axe):
    def __init__(self, beserker, silver_axe):
        super().__init__(beserker)
        self.silver_axe = silver_axe
    def __str__(self):
        return f"{self.beserker}, {self.silver_axe}"
class gold_axe(axe):
    def __init__(self, beserker, gold_axe):
        super().__init__(beserker)
        self.gold_axe = gold_axe
    def __str__(self):
        return f"{self.beserker}, {self.gold_axe}"
class diamond_axe(axe):
    def __init__(self, beserker, diamond_axe):
        super().__init__(beserker)
        self.diamond_axe = diamond_axe
    def __str__(self):
        return f"{self.beserker}, {self.diamond_axe}"