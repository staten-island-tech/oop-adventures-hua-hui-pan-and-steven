import uuid
class weapon:
    def __init__(self,equip_correct_class):
        self.equip_correct_class = equip_correct_class

class bronze_sword(weapon):
    def __init__(self, equip_correct_class, bronze_sword):
        super().__init__(equip_correct_class)

class silver_sword(weapon):


class gold_sword(weapon):


class diamond_sword(weapon):