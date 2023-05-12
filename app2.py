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
    def __init__(self, mage, silver_staff, attack, silver_shot):
        super().__init__(mage, attack, silver_shot)
        self.silver_staff = silver_staff
        self.silver_shot = silver_shot
    def __str__(self):
        return f"{self.mage}, {self.silver_staff}, {self.silver_shot}"
class gold_staff(staff):
    def __init__(self, mage, gold_staff, attack, gold_shot):
        super().__init__(mage, attack, gold_shot)
        self.gold_staff = gold_staff
        self.gold_shot = gold_shot
    def __str__(self):
        return f"{self.mage}, {self.gold_staff}, {self.gold_shot}"
class diamond_staff(staff):
    def __init__(self, mage, diamond_staff, attack, diamond_shot):
        super().__init__(mage, attack, diamond_shot)
        self.diamond_staff = diamond_staff
        self.diamond_shot = diamond_shot
    def __str__(self):
        return f"{self.mage}, {self.diamond_staff}, {self.diamond_shot}"
    
silver_shot = 5
gold_shot = 10
diamond_shot = 20




class axe:
    def __init__(self, beserker):
        self.beserker = beserker

class silver_axe(axe):
    def __init__(self, beserker, silver_axe, attack, silver_smash):
        super().__init__(beserker, attack, silver_smash)
        self.silver_axe = silver_axe
        self.silver_smash = silver_smash
    def __str__(self):
        return f"{self.beserker}, {self.silver_axe}, {self.silver_smash}"
class gold_axe(axe):
    def __init__(self, beserker, gold_axe, attack, gold_smash):
        super().__init__(beserker, attack, gold_smash)
        self.gold_axe = gold_axe
        self.gold_smash = gold_smash
    def __str__(self):
        return f"{self.beserker}, {self.gold_axe}, {self.gold_smash}"
class diamond_axe(axe):
    def __init__(self, beserker, diamond_axe, attack, diamond_smash):
        super().__init__(beserker, attack, diamond_smash)
        self.diamond_axe = diamond_axe
        self.diamond_smash = diamond_smash
    def __str__(self):
        return f"{self.beserker}, {self.diamond_axe}, {self.diamond_smash}"
    
silver_smash = 20
gold_smash = 30
diamond_smash = 50


