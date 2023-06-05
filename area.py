class area:
    def __init__(self,name):
        self.name = name

class shadow_castle(area):
    def __init__(self, name, location):
        super().__init__(name)
        self.location = location
    def __str__(self):
        return f"{self.name}, {self.location}"
    
class shadow_castle_second_floor(area):
    def __init__(self,name,location):
        super().__init__(name)
        self.location=location
    def __str__(self):
        return f"{self.name},{self.location}"
    
shadowcastle=area('shadow castle')
print('welcome to the shadow castle')






