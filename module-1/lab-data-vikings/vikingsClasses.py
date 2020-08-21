
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



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
        super().attack()

    def receiveDamage(self,damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f'A Saxon has received {self.damage} points of damage'
        else:
            return 'A Saxon has died in combat'    

        

# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self,oneViking):
        self.vikingArmy.append(oneViking)

    def addSaxon(self,oneSaxon):
        self.saxonArmy.append(oneSaxon)
        
    def vikingAttack(self):
        rand_saxon=random.choice(self.saxonArmy)
        rand_saxon.receiveDamage(oneViking.strength)
        rand_viking=random.choice(self.vikingArmy)
        if oneSaxon.health==0:
            self.saxonArmy.remove(oneSaxon)
            return oneSaxon.receiveDamage(oneViking.strength)

    def saxonAttack(self):
        oneViking.receiveDamage(oneSaxon.strength)
        if oneViking.receiveDamage(oneSaxon.strength)==0:
            self.vikingsArmy.remove(Viking)
            return oneViking.receiveDamage(oneSaxon.strength)

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy)==0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy)>0 or len(self.vikingArmy)>0:
            return 'Vikings and Saxons are still in the thick of battle.'


"""
vikingAttack() method
A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.

should be a function
should receive 0 arguments
should make a Saxon receiveDamage() equal to the strength of a Viking
should remove dead saxons from the army
should return result of calling receiveDamage() of a Saxon with the strength of a Viking
saxonAttack() method
The Saxon version of vikingAttack(). A Viking receives the damage equal to the strength of a Saxon.

should be a function
should receive 0 arguments
should make a Viking receiveDamage() equal to the strength of a Saxon
should remove dead vikings from the army
should return result of calling receiveDamage() of a Viking with the strength of a Saxon
"""
