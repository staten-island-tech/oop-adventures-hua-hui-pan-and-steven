import uuid
class user:
   def __init__(self,name):
      self.name=name

class Swordsmaster(user):
   def __init__(self,name,sword):
      super().__init__(name)
      self.sword= sword
   def __str__(self):
         return f"{self.name}, {self.sword}"
class Mage(user):
   def __init__(self,name,staff):
      super().__init__(name)
      self.staff=staff
   def __str__(self):
      return f"{self.name}, {self.staff}"
class Beserker(user):
   def __init__(self,name,axe):
      super().__init__(name)
      self.axe=axe
   def __str__(self):
      return f"{self.name}, {self.axe}"
   

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

swordsmasters=[]
mages=[]
beserkers=[]

def create_new_swordsmaster(name,sword):
    id = str(uuid.uuid4())
    new_swordsmaster= Swordsmaster(name,sword)
    swordsmasters.append(new_swordsmaster)
    for swordsmaster in swordsmasters:
        print(swordsmaster)

def create_new_mage(name,staff):
    id= str(uuid.uuid4())
    new_mage= Mage(name,staff)
    mages.append(new_mage)
    for mage in mages:
        print(mage)

def create_new_beserker(name,axe):
    id=str(uuid.uuid4())
    new_beserker=Beserker(name,axe)
    beserkers.append(new_beserker)
    for beserker in beserkers:
        print(beserker)

add_more_users= "y"
while add_more_users=="y":
    user_request = input("What type of user do you want to add? Ex. swordsmaster, mage, OR beserker? ")
    if use


        

    

