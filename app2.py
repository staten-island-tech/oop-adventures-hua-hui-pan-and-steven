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
    user_request = input("What type of user do you want to add? swordsmaster, mage, OR beserker? ")
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




        

    

