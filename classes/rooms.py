from random import  randint as rdt, choice
from classes.monster import Monster

#ROOM 1, mob commun entre 1 et 3
#ROOM 2, mob de type elite entre 1 et 3
#ROOM 3, mob de type boss entre 1 et 2 (99% de chance de tomber sur deux boss)

class Room :
    def __init__(self,number:int,monster_common:list,monster_elite:list,bosses:list,soron:list):
        if number == 1 :
            self.monsters = [Monster(choice(monster_common)) for _ in range(rdt(1,3))]
        if number == 2 :
            self.monsters = [Monster(choice(monster_elite)) for _ in range(rdt(1,3))]
        if number == 3 :
            if rdt(1,100) > 99 :
                self.monsters = [Monster(choice(bosses)) for _ in range(rdt(1,2))]
            else :
                self.monsters = [Monster(choice(bosses))]
            if rdt(1,400) == 400 :
                self.monsters.append(choice(self.monsters),Monster(soron))
                self.monsters.pop(0)

    def is_monsters_left(self)->bool :
        return len(self.monsters) != 0
    
    def check_monsters_dies(self) :
        for monster in self.monsters :
            if not(monster.is_alive()) :
                self.monsters.remove(monster)
                return self.monsters