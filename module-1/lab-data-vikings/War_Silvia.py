import random

class Pokemon: 
    def __init__(self, name, attack):
        self.name=name
        self.attack=attack
        self.health=100

    def aTtack(self):
            return f'{self.name} used {self.attack}!'

    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return f'{self.name} has received {damage} points of damage, Its health is: {self.health}'

        else: 
            return f"{self.name} has received {damage} points of damage,It's dead!"

       


class Pikachu(Pokemon):
    def __init__(self,name, attack):
        super().__init__(name,attack)   
    def battleCry(self):
        return f'{self.name} said: "Pika Pika chu!"'



class Charmander(Pokemon):
    def __init__(self,name, attack):
        super().__init__(name,attack)
   
    def battleCry(self):
        return f'{self.name} said: "Charmander!"'    

        
class Bulbasur(Pokemon):
    def __init__(self,name, attack):
        super().__init__(name,attack)
   
    def battleCry(self):
        return f'{self.name} said: "Bulba bulba!"'     

# Fight

class Fight:
    def __init__(self):
        self.pikachu=Pikachu('Pikachu','Thunder Shock')
        self.charmander=Charmander('Charmander','Ember')
        self.bulbasur=Bulbasur('Bulbasur','Vine Whip')

    def selectPokemons(self):
        self.pokemons=[self.pikachu,self.charmander,self.bulbasur]
        self.pokemon_player=input(f'Choose your Pokemon: {self.pikachu.name}, {self.charmander.name}  or {self.bulbasur.name}\n')
        while self.pokemon_player not in ('Pikachu','Charmander','Bulbasur'):
            print('You did not choose between those 3 Pokemon. Try again.\n')
            self.pokemon_player=input(f'Choose your Pokemon: {self.pikachu.name}, {self.charmander.name}  or {self.bulbasur.name}\n')  
            break 
        if self.pokemon_player==self.pikachu.name:
            self.pokemon_player=self.pikachu
        elif self.pokemon_player==self.charmander.name:
            self.pokemon_player=self.charmander
        elif self.pokemon_player==self.bulbasur.name:
            self.pokemon_player=self.bulbasur      
        self.pokemon_pc=random.choice(self.pokemons)
        while self.pokemon_pc==self.pokemon_player:
            self.pokemon_pc=random.choice(self.pokemons)
            break
        return f"You chose {self.pokemon_player.name}, you'll fight against {self.pokemon_pc.name}" 

    def pokemon_playerAttack(self):
        return self.pokemon_player.battleCry(),self.pokemon_player.aTtack(), self.pokemon_pc.receiveDamage(random.choice(range(1,101,1)))    
        

    def pokemon_pcAttack(self):
        return  self.pokemon_pc.battleCry(),self.pokemon_pc.aTtack(), self.pokemon_player.receiveDamage(random.choice(range(1,101,1)))


    def showStatus(self):
        if self.pokemon_player.health<=0:
            return f'{self.pokemon_player.name} lose against {self.pokemon_pc.name}'
        elif self.pokemon_pc.health<=0:
            return f'{self.pokemon_pc.name} lose against {self.pokemon_player.name}'
        elif self.pokemon_player.health>0 and self.pokemon_pc.health>0:
            return "Let's fight again!"
            


fight=Fight()
fight.selectPokemons()
fight.pokemon_playerAttack()
fight.pokemon_pcAttack()
fight.showStatus()

while fight.showStatus()=="Let's fight again":
    fight.pokemon_playerAttack()
    if fight.pokemon_player.health>0:
        fight.pokemon_pcAttack()
        fight.showStatus()
    else:
        fight.showStatus()

   


"""


"""

