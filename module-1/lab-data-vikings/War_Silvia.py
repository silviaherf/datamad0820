import random

class Pokemon: 
    def __init__(self, name, poke_type, attack):
        self.name=name
        self.poke_type=poke_type
        self.attack=attack

    def attack(self):
            return f'{self.name} used {self.attack}!'

    def receiveDamage(self):
        self.health=random.choice(range(50,101,1))
        self.damage=random.choice(range(1,101,1))
        self.health-=self.damage
        if self.health>0:
            return f'{self.name} has received {self.damage} points of damage'
        


class Pikachu(Pokemon):
    def __init__(self,name, attack):
        super().__init__(name,attack)
        super().attack()
        super().receiveDamage()
   
    def battleCry(self):
        return 'Pika Pika chu!'



class Charmander(Pokemon):
    def __init__(self,name, attack):
        super().__init__(name,attack)
        super().attack()
        super().receiveDamage()
   
    def battleCry(self):
        return 'Charmander!'    

        
class Bulbasur(Pokemon):
    def __init__(self,name, attack):
        super().__init__(name,attack)
        super().attack()
        super().receiveDamage()
   
    def battleCry(self):
        return 'Bulba bulba!'     

# Fight


dict_pokemon={
'Pikachu':['Pikachu','Electric','Thunder Shock'],'Charmander':['Charmander','Fire','Ember'],'Bulbasur':['Bulbasur','Grass','Vine Whip']}

class Fight:
    def __init__(self):
        self.pokemon_player=input('Choose your Pokemon: Pikachu, Charmander or Bulbasur')
        while pokemon_player not in dict_pokemon.keys():
            print('You did not choose between those 3 Pokemon. Try again.')
            self.pokemon_player=input('Choose your Pokemon: Pikachu, Charmander or Bulbasur')
        self.pokemons=['Pikachu','Charmander','Bulbasur']
        {'Pikachu':['Pikachu','Electric','Thunder Shock'],'Charmander':['Charmander','Fire','Ember'],'Bulbasur':['Bulbasur','Grass','Vine Whip']}
        
        self.pokemon_pc=random.choice(pokemons)
        while self.pokemon_pc==pokemon_player:
            self.pokemon_pc=random.choice(pokemons)
"""
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

"""
