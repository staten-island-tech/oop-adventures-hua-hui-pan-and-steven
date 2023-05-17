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








     

     
              


    