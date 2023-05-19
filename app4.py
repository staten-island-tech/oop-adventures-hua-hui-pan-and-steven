import uuid



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





