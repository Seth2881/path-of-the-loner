from random import randint as rdt, choice

class Monster :
    def __init__(self,monster:list[str,dict]):
        self.name = choice(monster[1]["name"])
        self.race = monster[0]

        self.type = monster[1]["type"]
        self.health = monster[1]["hp"]
        self.damage = monster[1]["damage"]
        self.is_magical = monster[1]["magical"]
        self.effects = monster[1]["effects"]

    def __str__(self):
        return f'{self.name} the {self.race}'

    def __str__(self)->str:
        return self.name
    
    def is_alive(self)->bool:
        return self.health>0
    
    def damage(self)->int:
        if self.is_alive() :
            return rdt(self.damage[0],self.damage[1])

    def get_hit(self,amount:int=0)->int :
        if self.is_alive() :
            if rdt(0,100) > 5 :
                if self.health-amount <=0 :
                    self.health = 0
                    return amount,self.health
                else :
                    self.health -= amount
                    return amount,self.health
            else :
                return ("missed","missed")