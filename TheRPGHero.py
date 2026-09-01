class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        pass

    def take_damage(self, amount):
        self.hp -= amount
        pass


arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print("Arthur's health has been reduced to:", arthur.hp)   # Expected: 90  
print("Morgana's health is still:", morgana.hp)            # Expected: 100

#this is pisay
