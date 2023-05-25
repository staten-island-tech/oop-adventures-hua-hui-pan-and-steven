<<<<<<< Updated upstream
import math
=======

>>>>>>> Stashed changes
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
shadow_metheor= 50

def get_input():
    attack= shadowslash_attack,shadowbomb_attack,shadowslam_attack,shadow_pierce,shadow_blast,shadow_shield_smash,shadow_javalin,shadow_hurricane,shadow_metheor
    while attack in[shadowslash_attack,shadowbomb_attack,shadowslam_attack,shadow_pierce,shadow_blast,shadow_shield_smash,shadow_javalin,shadow_hurricane,shadow_metheor]:
        if attack== shadowslash_attack:
            print("shadowslash -10 hp")
        elif attack==shadowbomb_attack:
            print("shadowbomb -15 hp")
        elif attack== shadowslam_attack:
            print("shadowslam -25 hp")
        elif attack== shadow_pierce:
            print("shadowslash -25 hp")
        elif attack== shadow_blast:
            print("shadowblast -30 hp")
        elif attack== shadow_shield_smash:
            print("shadow sheild smash -35 hp")
        elif attack== shadow_javalin:
            print("shadow javelin -40 hp")
        elif attack== shadow_hurricane:
            print("shadow hurricane -40 hp")
        elif attack== shadow_metheor:
            print("shadow metheor -50 hp")




     

     
              


    