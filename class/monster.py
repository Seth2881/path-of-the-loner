from random import randint as rdt
import json

with open("../data/player/ascendance.json","r",encoding='utf-8') as f :
    data_monsters = json.load(f)

class monster :
    def __init__(self,monster_type:list[str,dict]):
        pass

    def __str__(self):
        return self.name