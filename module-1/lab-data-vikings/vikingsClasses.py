
# Soldier


class Soldier: 
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
            return self.strength

    def receiveDamage(self,damage):
        self.damage=damage
        self.health-=self.damage
        


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name=name
        super().__init__(health,strength)
        super().attack()

    def receiveDamage(self,damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f'{self.name} has received {self.damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'





"""
A Viking is a Soldier with an additional property, their name. They also have a different receiveDamage() method and new method, battleCry().

Modify the Viking constructor function, have it inherit from Soldier, reimplement the receiveDamage() method for Viking, and add a new battleCry() method.

inheritance
Viking should inherit from Soldier
constructor function
should receive 3 arguments (name, health & strength)
should receive the name property as its 1st argument
should receive the health property as its 2nd argument
should receive the strength property as its 3rd argument

receiveDamage() method
(This method needs to be reimplemented for Viking because the Viking version needs to have different return values.)

should be a function
should receive 1 argument (the damage)
should remove the received damage from the health property
if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
if the Viking dies, it should return "NAME has died in act of combat"
battleCry() method
Learn more about battle cries.

should be a function
should receive 0 arguments
should return "Odin Owns You All!
"""
# Saxon


class Saxon:
    pass

# War


class War:
    pass
