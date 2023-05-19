import uuid
class user:
   def __init__(self,id,name):
      self.name=name
      self.id=id

class Swordsmaster(user):
   def __init__(self,id,name,sword):
      super().__init__(name,id)
      self.sword= sword
   def __str__(self):
         return f"{self.name},{self.id}, {self.sword}"
class Mage(user):
   def __init__(self,id,name,staff):
      super().__init__(name,id)
      self.staff=staff
   def __str__(self):
      return f"{self.name},{self.id} ,{self.staff}"
class Beserker(user):
   def __init__(self,id,name,axe):
      super().__init__(name,id)
      self.axe=axe
   def __str__(self):
      return f"{self.name},{self.id}, {self.axe}"

swordsmasters=[]
mages=[]
beserkers=[]

def create_new_swordsmaster(name,sword):
    id= str(uuid.uuid4())
    new_swordsmaster= Swordsmaster(name,id,sword)
    swordsmasters.append(new_swordsmaster)
    for swordsmaster in swordsmasters:
        print(swordsmaster)

def create_new_mage(name,staff):
    id= str(uuid.uuid4())
    new_mage= Mage(name,id,staff)
    mages.append(new_mage)
    for mage in mages:
        print(mage)

def create_new_beserker(name,axe):
    id=str(uuid.uuid4())
    new_beserker=Beserker(name,id,axe)
    beserkers.append(new_beserker)
    for beserker in beserkers:
        print(beserker)

no_more_users="n"
add_more_users= "y"
while add_more_users=="y":
    user_request = input("What type of user do you want to add? Ex. swordsmaster, mage, OR beserker? ")
    if user_request.upper()=="swordsmaster":
        name=input("enter name")
        sword=input("what type of sword")
        create_new_swordsmaster(name,sword)
    elif user_request.upper()=="mage":
        name=input("enter name")
        staff=input("what type of staff")
        create_new_mage(name,staff)
    elif user_request.upper()=="beserker":
        name=input("enter name")
        axe=input("what type of axe")
    else:
        print("something went wrong")
    still_continue=input("would you like to add more characters y/n").upper()
    add_more_users= still_continue
while no_more_users=="n":
    if still_continue=="n":
        print("welcome to your new adventure")
    else:
        print("something went wrong")


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
shadowbomb_attack= 15
shadowslam_attack=25

Hp=50
Hp=75
Hp=100

class bosses:
     def __init__(self, name, attack):
          self.name = name
          self.attack = attack

class shadow_general(bosses):
    def __init__(self, name, attack, shadow_pierce, shadow_blast):
          super().__init__(name, attack)
          self.shadow_pierce = shadow_pierce
          self.shadow_blast = shadow_blast
    def __str__(self):
        return f"{self.name},{self.attack},{self.shadow_pierce},{self.shadow_blast}"
class shadow_guardian(bosses):
    def __init__(self, name, attack, shadow_shield_smash, shadow_javalin):
          super().__init__(name, attack)
          self.shadow_shield_smash = shadow_shield_smash
          self.shadow_javalin = shadow_javalin
    def __str__(self):
         return f"{self.name},{self.attack},{self.shadow_shield_smash},{self.shadow_javalin}"
class shadow_king(bosses):
    def __init__(self, name, attack, shadow_hurricane, shadow_blast, shadow_metheor):
          super().__init__(name, attack)
          self.shadow_hurricane = shadow_hurricane
          self.shadow_blast = shadow_blast
          self.shadow_metheor = shadow_metheor
    def __str__(self):
         return f"{self.name},{self.attack},{self.shadow_hurricane},{self.shadow_blast},{self.shadow_metheor}"
Hp=125
Hp=150
Hp=180
shadow_pierce = 25
shadow_blast = 30
shadow_shield_smash = 35
shadow_javalin = 40
shadow_hurricane = 40
shadow_metheor = 50   

def get_input():
    attack=""
    while not attack in[{10},shadowslash_attack,{15},shadowbomb_attack,{25},shadowslam_attack,{25},shadow_pierce,{}                        ]

        

    

