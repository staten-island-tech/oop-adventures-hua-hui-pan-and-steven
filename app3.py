class area:
    def __init__(self,name):
        self.name = name

class shadow_castle(area):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location
    def __str__(self):
        return f"{self.name}, {self.location}"
<<<<<<< HEAD
    
=======
    
class shadow_castle_second_floor(area):
    def __init__(self,name,location):
        super().__init__(name)
        self.location=location
    def __str__(self):
        return f"{self.name},{self.location}"
    
def x ():
   
>>>>>>> 12e64b291bfd7aa32d8d1557ab50f9989d4d390d
