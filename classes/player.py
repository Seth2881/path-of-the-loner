from random import randint as rdt
import json

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

class Weapon :
    def __init__(self,player_weapon:list[str,dict]=["none",{}]):

        if player_weapon[0] != "none" :
            self.damage = player_weapon[1]["damage"]
            self.ismagical = player_weapon[1]["magical"]
            self.bonus = player_weapon[1]["bonus"]
            self.name = player_weapon[0]

            if self.name == "hammer":
                self.canattack = True
        else :
            self.name = 'feast'
            self.damage = None
            self.ismagical = False
            self.bonus = []

    def __str__(self)->str:
        return self.name
    
    def attack(self)->int :
        if self.ismagical == False :
            if self.name == "hammer" and self.canattack :
                self.canattack = False
                return rdt(self.damage[0],self.damage[1])
            elif self.name == "hammer" and not self.canattack :
                self.canattack = True
                print('you can only attack every two turn with the hammer')
                return 0
            else :
                return rdt(self.damage[0],self.damage[1])
        else :
            return rdt(self.damage[0],self.damage[1])            

class Character() :
    def __init__(self,player_type:list[str,dict]=["default",data_type["default"]],player_weapon:Weapon=Weapon(),player_armor:Armor=Armor()):

        self.weapon = player_weapon
        self.armor = player_armor
        if self.weapon.name == "feast" :
            self.weapon.damage = player_type[1]["dgt_hand"]

        self.ascendence = player_type[0]

        self.total_health = player_type[1]["hp"]+player_armor.defence
        self.armor_health = player_armor.defence

        self.agility = player_type[1]["agility"]
        self.attack_order = player_type[1]["attack_order"]

        self.is_magical = False

        if player_type[0] == "archer" :
            self.arrow_count = player_type[1]["arrow_count"]
        if player_type[0] == "magician" :
            self.mana_count = player_type[1]["mana_count"]
            self.is_magical = True

    def __str__(self):
        return self.ascendence

    def get_player_info(self)->None :
        print("character")
        input("__________________________")
        for key,value in self.__dict__.items() :
            if str(value) not in ["",'[]']:
                print(key,':',value)
        print("__________________________")
        print()
        print("weapon")
        input("__________________________")
        for key,value in self.weapon.__dict__.items() :
            if str(value) not in ['[]']:
                print(key,':',value)
        print("__________________________")
        print()
        print("armor")
        input("__________________________")
        for key,value in self.armor.__dict__.items() :
            if str(value) not in ['[]','0']:
                print(key,':',value)
        input("")
        
    def is_alive(self)->bool :
        return self.total_health>0

    def damage(self)->int :
        if self.is_alive() :
            return self.weapon.attack()
    
    def get_health_down(self,amount=0)->int :
        try :
            if self.is_alive() :
                miss = rdt(0,100)
                if miss > self.agility :
                    if self.total_health-amount <= 0:
                        self.total_health=0
                        return amount,self.total_health
                    elif not(self.armor.is_broke()):
                        self.total_health -= amount
                        self.armor.get_hit(amount)
                        return amount,self.total_health
                    else :
                        self.total_health -= amount
                        return amount,self.total_health
                else :
                    return 'missed','missed'
        except :
            return 'missed','missed'
                
    def show_health(self)->None :
        print(f'{self.ascendence} as {self.total_health}HP')