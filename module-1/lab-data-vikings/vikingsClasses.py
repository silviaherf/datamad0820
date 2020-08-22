
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
        self.vikingArmy =[]
        self.saxonArmy =[]

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        self.saxon=random.choice(self.saxonArmy)
        self.viking=random.choice(self.vikingArmy)
        saxon_health=self.saxon.receiveDamage(self.viking.attack())
        if self.saxon.health<=0:
            self.saxonArmy.remove(self.saxon) 
        return saxon_health       

    def saxonAttack(self):
        self.saxon=random.choice(self.saxonArmy)
        self.viking=random.choice(self.vikingArmy)
        viking_health=self.viking.receiveDamage(self.saxon.attack())
        if self.viking.health<=0:
            self.vikingArmy.remove(self.viking)   
        return viking_health

    def showStatus(self):
        if (len(self.saxonArmy)==0):
            return 'Vikings have won the war of the century!'
        elif (len(self.vikingArmy)==0):
            return 'Saxons have fought for their lives and survive another day...'
        elif (len(self.saxonArmy)>0) or (len(self.vikingArmy)>0):
            return 'Vikings and Saxons are still in the thick of battle.'



