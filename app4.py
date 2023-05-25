import uuid

import Game
start = Game
get_input()





swordsmaster =[]
mage = []
beserker = []

class user:
    def __init__(self, name):
        self.name = name

class swordsmaster(user):
   def __init__(self,name,sword):
      super().__init__(name)
      self.sword= sword
   def __str__(self):
         return f"{self.name}, {self.sword}"
class mage(user):
   def __init__(self,name,staff):
      super().__init__(name)
      self.staff=staff
   def __str__(self):
      return f"{self.name}, {self.staff}"
class beserker(user):
   def __init__(self,name,axe):
      super().__init__(name)
      self.axe=axe
   def __str__(self):
      return f"{self.name}, {self.axe}"





shadow_soldiers = []
shadow_golem = []
shadow_giants = []

import uuid
class mobs:
    def __init__(self,name,attack):
        self.name=name
        self.attack=attack

class shadow_soldiers(mobs):
    def __init__(self,name,attack,shadowslash):
        super().__init__(name,attack)
        self.shadowslash= shadowslash
    def __str__(self):
            return f"{self.name},{self.attack},{self.shadowslash}"
class shadow_golem(mobs):
    def __init__(self,name,attack,shadowslash,shadowbomb):
          super().__init__(name,attack,shadowslash)
          self.shadowbomb=shadowbomb
          self.shadowslash=shadowslash
    def __str__(self):
          return f"{self.name},{self.attack},{self.shadowslash},{self.shadowbomb}"
class shadow_giants(mobs):
    def __init__(self,name,attack,shadowslash,shadowbomb,shadowslam):
          super().__init__(self,name,attack,shadowslash,shadowbomb)
          self.shadowslam=shadowslam
          self.shadowbomb=shadowbomb
          self.shadowslash=shadowslash
    def __str__(self):
          return f"{self.name},{self.attack},{self.shadowslash}{self.shadowbomb},{self.shadowslam}"

shadowslash_attack= 10
shadowbomb_attack= 25
shadowslam_attack= 40

Hp=50
Hp=100
Hp=150





shadow_general = []
shadow_guardian =[]
shadow_king = []

class bosses:
     def __init__(self, name, attack):
          self.name = name
          self.attack = attack

class shadow_general(bosses):
    def __init__(self, name, attack, shadow_pierce):
          super().__init__(name, attack)
          self.shadow_pierce = shadow_pierce
    def __str__(self):
        return f"{self.name},{self.attack},{self.shadow_pierce}"
class shadow_guardian(bosses):
    def __init__(self, name, attack, shadow_shield_smash):
          super().__init__(name, attack)
          self.shadow_shield_smash = shadow_shield_smash
    def __str__(self):
         return f"{self.name},{self.attack},{self.shadow_shield_smash}"
class shadow_king(bosses):
    def __init__(self, name, attack, shadow_blast, shadow_metheor):
          super().__init__(name, attack)
          self.shadow_blast = shadow_blast
          self.shadow_metheor = shadow_metheor
    def __str__(self):
         return f"{self.name},{self.attack},{self.shadow_blast},{self.shadow_metheor}"

shadow_pierce = 25
shadow_blast = 30
shadow_shield_smash = 35
shadow_metheor = 50






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














print("Start the adventure!")

def user(swordsmaster, mage, beserker):
   if user == swordsmaster:
      print("Play as swordsmaster")
      print("You get silver sowrd!")
   elif user == mage:
      print("Play as mage")
      print("You get silver staff!")
   elif user == beserker:
      print("Play as beserker")
      print("You get silver axe!")
   else:
      print("Did you even select a hero?")

def get_input():
    attack=""
    while attack in [shadowslash_attack, shadowbomb_attack, shadowslam_attack, shadow_pierce, shadow_blast, shadow_shield_smash, shadow_metheor]:
        if attack == shadowslash_attack:
            print("shadowslash_attack -10 hp")
        if attack == shadowbomb_attack:
            print("shadowbomb_attack -25 hp")
        if attack == shadowslam_attack:
            print("shadowslam_attack -40 hp")
        if attack == shadow_pierce:
            print("shadow_pierce -25 hp")
        if attack == shadow_blast:
            print("shadow_blast -30 hp")
        if attack == shadow_shield_smash:
            print("shadow_shield_smash -35 hp")
        if attack == shadow_metheor:
            print("shadow_metheor -50 hp")



def get_input(swordsmaster):
    attack=""
    while attack in [silver_slash, gold_slash, diamond_slash]:
        if attack == silver_slash:
            print("silver_slash -10 hp enemy")
        if attack == gold_slash:
            print("gold_slash -20 hp enemy")
        if attack == diamond_slash:
            print("diamond_slash -45 hp enemy")



def get_input(mage):
    attack=""
    while attack in [silver_shot, gold_shot, diamond_shot]:
        if attack == silver_shot:
            print("silver_shot -10 hp enemy")
        if attack == gold_shot:
            print("gold_shot -20 hp enemy")
        if attack == diamond_shot:
            print("diamond_shot -45 hp enemy")



def get_input(beserker):
    attack=""
    while attack in [silver_smash, gold_smash, diamond_smash]:
        if attack == silver_smash:
            print("silver_shot -20 hp enemy")
        if attack == gold_smash:
            print("gold_smash -35 hp enemy")
        if attack == diamond_smash:
            print("diamond_smash -50 hp enemy")