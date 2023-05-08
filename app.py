import uuid
class user:
    def __init__(self,name):
     self.name=name

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
      
      