import random
class Adventurer:
    def __init__(self, name):
        self.name = name
        self.strength = random.randint(1,20)
        self.constitution = random.randint(5,15)
        #constitution（体质）--decides the maximum of the characters life
        self.bag:list[Item] = [Item("wooden sword", 0, 1)]
        self.hitpoints = self.constitution+random.randint(15,50)
        #decides whether or not the hero lives-- the amount of life left；≤0 the character dies

class Item:
    def __init__(self, name, min_damage, max_damage):
        if name!=None:
            self.name = name
        else:
            self.name = "Error, unknown item"

        self.min_damage = min_damage
        self.max_damage = max_damage

class Monster:
    def __init__(self, name, min_damage, max_damage, hitpoints):
        """initializes the monster with its attributes"""
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.hitpoints = hitpoints
    @classmethod
    def createMonster(cls):#class function
        """create a random monster"""
        monsters = ["ghost 👻", "zombie 🧟", "python 🐍", "chinese dragon 🐲"]
        name = random.choice(monsters)
        if name=="ghost 👻":
            return Monster(name, random.randint(0,1), random.randint(2,5),3)
        elif name=="zombie 🧟":
            return Monster(name, random.randint(1,3), random.randint(5,6),3)
        elif name=="python 🐍":
            return Monster(name, random.randint(5,6), random.randint(7,8),5)
        elif name=="chinese dragon 🐲":
            return Monster(name, random.randint(7,9), random.randint(10,12),8)

class Room:
    """the room has a monster and item(treasure) that could be gained by the adventurer
    if he or she wins the battle which takes place here"""
    #attributes: treasure(Item)&monster

    def __init__(self):
        self.create_monsterAndTreasure()
    def create_monsterAndTreasure(self):
        items = ["Celestial Bronze sword", "silver dagger", "imperial gold spear", "Apollo's golden bow"]
        name = random.choice(items)
        if name=="Celestial Bronze sword":
            self.treasure = Item(name, random.randint(5,7), random.randint(8,10))
        elif name=="silver dagger":
            self.treasure = Item(name, random.randint(2, 3), random.randint(4, 5))
        elif name=="imperial gold spear":
            self.treasure = Item(name, random.randint(3, 5), random.randint(6,8))
        elif name=="Apollo's golden bow":
            self.treasure = Item(name, random.randint(8, 9), random.randint(10, 12))

        self.monster = Monster.createMonster()
    @staticmethod
    def calculate_damage(attacker:Item|Monster, defender:Monster|Adventurer):
        """calculate the damage done by the attacker to the defender
        Returns true if the combat resulted in the death of the defender"""
        damage_done = random.randint(attacker.min_damage, attacker.max_damage)
        defender.hitpoints-=damage_done
        print(f"{attacker.name} caused {damage_done} damage to {defender.name} which has {defender.hitpoints} left!")

        if defender.hitpoints<=0:
            return True
        return False


    def enter_and_combat(self,hero:Adventurer):
        """The hero enters the cave and fights with the monster in the cave"""
        print(f"{hero.name} enters the room and looks around...")
        heal = [random.randint(9,12) for i in range(3,5)]

        combat_done = False
        while not combat_done:
            if random.randint(0,1)==1:#hero goes first
                item = random.choice(hero.bag)
                combat_done = Room.calculate_damage(item,self.monster)
            else:
                combat_done = Room.calculate_damage(self.monster, hero)

        if hero.hitpoints>=0:
            hero.bag.append(self.treasure)
            print(f"{hero.name} adds a {self.treasure.name} to their bag!")
            a = random.choice(heal)
            hero.hitpoints+=a
            print(f"{hero.name} adds {a} to their hitpoints")
            return "win!"
        return "loose"
class Cave:
    """Caves have many rooms, here there are 8 rooms in the cave!
    the ideal place for adventurers to explore!"""
    def __init__(self):
        self.rooms:[Room]= []
        for i in range(0,8):
            self.rooms.append(Room())

    def explore(self, hero):
        """gives the outline & outcome of the adventurer's trip in the caves"""
        l = ["It is with sincere regret that we must relay, in light of the subsequent happenings, the hero has been lost","We feel it our duty to impart, with genuine sorrow, that owing to the events that transpired, the hero has fallen","With a weighty heart, we must confirm that as a consequence of the unfolding circumstances, the hero is no more"]
        for room in self.rooms:
            result = room.enter_and_combat(hero)
            if result=="loose":
                _l = random.choice(l)
                print(_l)
                return #Exit the entire function using the return statement
            else:
                print(
                    f"For the record: your valiant penetration of an additional chamber, {hero.name}, is duly noted. "
                    f"Your inventory presently comprises {len(hero.bag)} items, and your vitality metric stands at {hero.hitpoints} hit points— "
                )
        print(f"CONGRATULATIONS! a state deemed 'satisfactory' in light of prevailing circumstances.")

#START PLAYING!
hero = Adventurer("Nithaniel")
cave = Cave()
cave.explore(hero)





















