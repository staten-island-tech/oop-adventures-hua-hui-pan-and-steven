import uuid
class weapon:
    def __init__(self,equip_correct_class):
        self.equip_correct_class = equip_correct_class

class silver_sword(weapon):
    def __init__(self, equip_correct_class, silver_sword):
        super().__init__(equip_correct_class)
        self.silver_sword = silver_sword
    def __str__(self):
        return f"{self.equip_correct_class}, {self.silver_sword}"
    
class gold_sword(weapon):
    def __init__(self, equip_correct_class, gold_sword):
        super().__init__(equip_correct_class)
        self.gold_sword = gold_sword
    def __str__(self):
        return f"{self.equip_correct_class}, {self.gold_sword}"
    
class diamond_sword(weapon):
    def __init__(self, equip_correct_class, diamond_sword):
        super().__init__(equip_correct_class)
        self.diamond_sword = diamond_sword
    def __str__(self):
        return f"{self.equip_correct_class}, {self.diamond_sword}"