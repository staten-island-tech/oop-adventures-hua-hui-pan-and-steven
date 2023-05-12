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

     

     
              


    