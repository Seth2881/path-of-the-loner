from random import randint as rdt, choice

class Monster :
    def __init__(self,monster:list[str,dict]):
        self.name = choice(monster[1]["name"]) if type(monster[1]["name"]) == dict else(monster[1]["name"])

        self.type = monster[1]["type"]
        self.health = monster[1]["hp"]
        self.damage = monster[1]["damage"]
        self.is_magical = monster[1]["magical"]
        self.effects = monster[1]["effects"]

    def __str__(self)->str:
        return self.name
    
    def is_alive(self)->bool:
        return self.health>0
    
    def deals_damage(self)->int:
        if self.is_alive() :
            return rdt(self.damage[0],self.damage[1])

    def get_hit(self,amount:int)->int :
        if self.is_alive() :
            if self.health-amount <=0 :
                self.health = 0
                return self.health
            else :
                self.health -= amount
                return self.health