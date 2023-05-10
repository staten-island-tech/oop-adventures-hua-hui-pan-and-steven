import uuid

class sword:
    def __init__(self,swordsmaster):
        self.swordsmaster = swordsmaster

class silver_sword(sword):
    def __init__(self, swordsmaster, silver_sword):
        super().__init__(swordsmaster)
        self.silver_sword = silver_sword
    def __str__(self):
        return f"{self.swordsmaster}, {self.silver_sword}"
class gold_sword(sword):
    def __init__(self, swordsmaster, gold_sword):
        super().__init__(swordsmaster)
        self.gold_sword = gold_sword
    def __str__(self):
        return f"{self.swordsmaster}, {self.gold_sword}"
class diamond_sword(sword):
    def __init__(self, swordsmaster, diamond_sword):
        super().__init__(swordsmaster)
        self.diamond_sword = diamond_sword
    def __str__(self):
        return f"{self.swordsmaster}, {self.diamond_sword}"
    



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

class silver_staff(axe):
    def __init__(self, beserker, silver_axe):
        super().__init__(beserker)
        self.silver_axe = silver_axe
    def __str__(self):
        return f"{self.beserker}, {self.silver_axe}"
class gold_staff(axe):
    def __init__(self, beserker, gold_axe):
        super().__init__(beserker)
        self.gold_axe = gold_axe
    def __str__(self):
        return f"{self.beserker}, {self.gold_axe}"
class diamond_staff(axe):
    def __init__(self, beserker, diamond_axe):
        super().__init__(beserker)
        self.diamond_axe = diamond_axe
    def __str__(self):
        return f"{self.beserker}, {self.diamond_axe}"