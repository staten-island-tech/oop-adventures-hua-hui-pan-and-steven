import random



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


import random
class weapon:
    def __init__(self,attack,weapon):
        self.attack=attack
        self.weapon=weapon

class longsword(weapon):
    def __init__(self,attack,weapon,piercestab):
        super().__init__(attack,weapon)
        self.piercestab=piercestab
    def moves():
        piercestab=50
        attack=40
        if user_request==
    
        

    
class greatstaff(weapon): 
    def __init__(self,attack,weapon,lightning):
        super().__init__(self,attack ,weapon)
        self.lightning=lightning
        lightning=80
        attack=50
    
class devilaxe(weapon):
    def __init__(self, attack,weapon,ragespin):
        super().__init__(attack,weapon)
        self.ragespin=ragespin
        ragespin=90
        attack=60
   

