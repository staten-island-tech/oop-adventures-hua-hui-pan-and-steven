
class weapon:
    def __init__(self,attack,weapon):
        self.attack=attack
        self.weapon=weapon

class longsword(weapon):
    def __init__(self,attack,weapon,piercestab):
        super().__init__(attack,weapon)
        self.piercestab=piercestab
    
    
    
class greatstaff(weapon): 
    def __init__(self,attack,weapon,frostbolt,fireball,arcanemissile):
        super().__init__(self,attack ,weapon)
        self.frostbolt=frostbolt
        self.fireball=fireball
        self.arcanemissile=arcanemissile
        
    
class devilaxe(weapon):
    def __init__(self, attack,weapon,ragingstrike,whirlwind,Berserkerage):
        super().__init__(attack,weapon)
        self.ragingstrike=ragingstrike
        self.whirlwind=whirlwind
        self.Berserkerage=Berserkerage
   

