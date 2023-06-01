import random
import uuid

class User:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.health = 100

    def choose_attack(self):
        raise NotImplementedError("Subclasses must implement choose_attack method.")

    def __str__(self):
        return f"{self.name}, {self.id}"

class Swordsmaster(User):
    def __init__(self, id, name, sword):
        super().__init__(id, name)
        self.sword = sword

    def choose_attack(self):
        return random.choice(["Slash", "Thrust", "Parry"])

    def __str__(self):
        return f"{super().__str__()}, {self.sword}"

class Mage(User):
    def __init__(self, id, name, staff):
        super().__init__(id, name)
        self.staff = staff

    def choose_attack(self):
        return random.choice(["Fireball", "Frostbolt", "Arcane Missile"])

    def __str__(self):
        return f"{super().__str__()}, {self.staff}"

class Berserker(User):
    def __init__(self, id, name, axe):
        super().__init__(id, name)
        self.axe = axe

    def choose_attack(self):
        return random.choice(["Raging Strike", "Whirlwind", "Berserker Rage"])

    def __str__(self):
        return f"{super().__str__()}, {self.axe}"

class Mob:
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
        self.health = 100

    def choose_move(self):
        raise NotImplementedError("Subclasses must implement choose_move method.")

    def __str__(self):
        return f"{self.name}, {self.attack}"

class ShadowSoldiers(Mob):
    def __init__(self, name, attack, shadowslash):
        super().__init__(name, attack)
        self.shadowslash = shadowslash

    def choose_move(self):
        return self.shadowslash

    def __str__(self):
        return f"{super().__str__()}, {self.shadowslash}"

class ShadowGolem(Mob):
    def __init__(self, name, attack, shadowslash, shadowbomb):
        super().__init__(name, attack)
        self.shadowbomb = shadowbomb
        self.shadowslash = shadowslash

    def choose_move(self):
        return random.choice([self.shadowslash, self.shadowbomb])

    def __str__(self):
        return f"{super().__str__()}, {self.shadowslash}, {self.shadowbomb}"

class ShadowGiants(Mob):
    def __init__(self, name, attack, shadowslash, shadowbomb, shadowslam):
        super().__init__(name, attack)
        self.shadowslam = shadowslam
        self.shadowbomb = shadowbomb
        self.shadowslash = shadowslash

    def choose_move(self):
        return random.choice([self.shadowslash, self.shadowbomb, self.shadowslam])

    def __str__(self):
        return f"{super().__str__()}, {self.shadowslash}, {self.shadowbomb}, {self.shadowslam}"

class Bosses(Mob):
    pass

class ShadowGeneral(Bosses):
    def __init__(self, name, attack, shadow_pierce, shadow_blast):
        super().__init__(name, attack)
        self.shadow_pierce = shadow_pierce
        self.shadow_blast = shadow_blast

    def choose_move(self):
        return random.choice([self.shadow_pierce, self.shadow_blast])

    def __str__(self):
        return f"{super().__str__()}, {self.shadow_pierce}, {self.shadow_blast}"

class ShadowGuardian(Bosses):
    def __init__(self, name, attack, shadow_shield_smash, shadow_javelin):
        super().__init__(name, attack)
        self.shadow_shield_smash = shadow_shield_smash
        self.shadow_javelin = shadow_javelin

    def choose_move(self):
        return random.choice([self.shadow_shield_smash, self.shadow_javelin])

    def __str__(self):
        return f"{super().__str__()}, {self.shadow_shield_smash}, {self.shadow_javelin}"

class ShadowKing(Bosses):
    def __init__(self, name, attack, shadow_hurricane, shadow_blast, shadow_meteor):
        super().__init__(name, attack)
        self.shadow_hurricane = shadow_hurricane
        self.shadow_blast = shadow_blast
        self.shadow_meteor = shadow_meteor

    def choose_move(self):
        return random.choice([self.shadow_hurricane, self.shadow_blast, self.shadow_meteor])

    def __str__(self):
        return f"{super().__str__()}, {self.shadow_hurricane}, {self.shadow_blast}, {self.shadow_meteor}"

swordsmasters = []
mages = []
berserkers = []

def create_new_swordsmaster(name, sword):
    id = str(uuid.uuid4())
    new_swordsmaster = Swordsmaster(id, name, sword)
    swordsmasters.append(new_swordsmaster)
    print("Swordsmaster added:")
    print(new_swordsmaster)

def create_new_mage(name, staff):
    id = str(uuid.uuid4())
    new_mage = Mage(id, name, staff)
    mages.append(new_mage)
    print("Mage added:")
    print(new_mage)

def create_new_berserker(name, axe):
    id = str(uuid.uuid4())
    new_berserker = Berserker(id, name, axe)
    berserkers.append(new_berserker)
    print("Berserker added:")
    print(new_berserker)

add_more_users = "y"

while add_more_users == "y":
    user_request = input("What type of user do you want to add? Swordsmaster, Mage, or Berserker? ")
    if user_request.lower() == "swordsmaster":
        name = input("Enter name: ")
        sword = input("What type of sword? ")
        create_new_swordsmaster(name, sword)
    elif user_request.lower() == "mage":
        name = input("Enter name: ")
        staff = input("What type of staff? ")
        create_new_mage(name, staff)
    elif user_request.lower() == "berserker":
        name = input("Enter name: ")
        axe = input("What type of axe? ")
        create_new_berserker(name, axe)
    else:
        print("Invalid user type.")
    still_continue = input("Would you like to add more characters? (y/n): ").lower()
    add_more_users = still_continue

chosen_user = random.choice(swordsmasters + mages + berserkers)
print(f"{chosen_user.name}, choose your attack:")
chosen_attack = chosen_user.choose_attack()
print(f"{chosen_user.name} uses {chosen_attack}!")

# Define calculate_damage function
def calculate_damage(attack):
    return random.randint(10, 20)

mobs = [ShadowSoldiers("Shadow Soldiers", "Normal Attack", "Shadow Slash"),
        ShadowGolem("Shadow Golem", "Normal Attack", "Shadow Slash", "Shadow Bomb"),
        ShadowGiants("Shadow Giants", "Normal Attack", "Shadow Slash", "Shadow Bomb", "Shadow Slam")]

mob = random.choice(mobs)
print(f"The {mob.name} attacks with {mob.attack}!")

while chosen_user.health > 0 and mob.health > 0:
    chosen_attack = input(f"{chosen_user.name}, choose your attack: ")
    if chosen_attack not in ["Slash", "Thrust", "Parry", "Fireball", "Frostbolt", "Arcane Missile", "Raging Strike", "Whirlwind", "Berserker Rage"]:
        print("Invalid attack. Please choose a valid attack.")
        continue

    player_damage = calculate_damage(chosen_attack)
    mob_damage = calculate_damage(mob.attack)

    chosen_user.health -= mob_damage
    mob.health -= player_damage

    print(f"{chosen_user.name} deals {player_damage} damage to the {mob.name}!")
    print(f"The {mob.name} deals {mob_damage} damage to {chosen_user.name}!")

    if chosen_user.health <= 0:
        print(f"{chosen_user.name} has been defeated!")
        break

    if mob.health <= 0:
        print(f"The {mob.name} has been defeated!")
        break

print("Battle ended.")
