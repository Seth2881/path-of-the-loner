from random import randint as rdt
import json

with open("data/spells.json","r",encoding='utf-8') as f:
    data_spells = json.load(f)

with open("data/ascendance.json","r",encoding='utf-8') as f :
    data_type = json.load(f)

with open("data/weapons.json","r",encoding='utf-8') as f :
    data_weapon = json.load(f)

with open("data/armors.json","r",encoding='utf-8') as f :
    data_armor = json.load(f)

with open("data/ascendance.json","r",encoding='utf-8') as f :
    data_monsters = json.load(f)

class Armor :
    def __init__(self,player_armor:list[str,dict]=["leather_armor",data_armor["leather_armor"]]):

        self.name = player_armor[0]

        self.defence = player_armor[1]["defence"]
        self.self_damage = player_armor[1]["self_damage"]
        self.bonus_damage = player_armor[1]["bonus_zone_damage"]
        self.thorns = player_armor[1]["thorns"]
    
    def __str__(self)->str:
        return self.name
    
    def is_broke(self)->bool:
        return self.defence <= 0

    def get_hit(self,amount:int)->int:
        if not(self.is_broke()) :
            self.defence -= amount
            if self.is_broke() :
                print('your armor broke ! armor effects no longer apply.')
            return self.defence
        

    def get_effect() :
        pass