from random import randint as rdt
import json

#.items() pour convertir en list de tuples cle_valeur puis on réecris 
# la liste afin de pouvoir modifier les valeurs si besoin

with open("../data/player/ascendance.json","r",encoding='utf-8') as f :
    data_type = json.load(f).items()
    for ele in data_type :
        data_type.index(ele) = [ele[0],ele[1]]

with open("../data/player/weapon.json","r",encoding='utf-8') as f :
    data_weapon = json.load(f).items()
    for ele in data_weapon :
        data_weapon.index(ele) = [ele[0],ele[1]]

with open("../data/player/ascendance.json","r",encoding='utf-8') as f :
    data_armor = json.load(f).items()
    for ele in data_armor :
        data_armor.index(ele) = [ele[0],ele[1]]

class armor :
    def __init__(self,player_armor:list=["leather",{"defence":25}]):
        self.defence = player_armor[1]["defence"]
        self.name = player_armor[0]
    
    def getArmorName(self) :
        return self.name

class weapon :
    def __init__(self,player_weapon:list=["sword",{"damage" : [5,10]}]):
        self.damage = player_weapon[1]["damage"]
        self.name = player_weapon[0]

    def getWeaponName(self):
        return self.name

class character(weapon,armor) :
    def __init__(self,player_type:list=["sword",{"hp" : 60,"dgt_hand" : [2,4]}]):
        self.total_health = player_type[1]["hp"]+armor.defence
        self.dgt_hand = player_type[1]["dgt_hand"]
        self.damage = weapon.damage

    def get_damage(self) :
        return rdt(self.damage[0],self.damage[1])
        
    def get_hand_damage(self) :
        return rdt(self.dgt_hand[0],self.dgt_hand[1])