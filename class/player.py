from random import randint as rdt
import json

with open("data/ascendance.json","r",encoding='utf-8') as f :
    data_type = json.load(f)

with open("data/weapons.json","r",encoding='utf-8') as f :
    data_weapon = json.load(f)

with open("data/armors.json","r",encoding='utf-8') as f :
    data_armor = json.load(f)

class armor :
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

class weapon :
    def __init__(self,player_weapon:list[str,dict]=["none",{}]):

        if player_weapon[0] != "none" :
            self.damage = player_weapon[1]["damage"]
            self.ismagical = player_weapon[1]["magical"]
            self.bonus = player_weapon[1]["bonus"]
            self.name = player_weapon[0]

            if self.name == "hammer":
                self.canattack = True
        self.name = 'feast'
        self.damage = None
        self.ismagical = False
        self.bonus = []

    def __str__(self)->str:
        return self.name
    
    def attack(self)->int :
        if self.ismagical == False :
            if self.name == "hammer" and self.canattack == True :
                self.canattack = False
                return rdt(self.damage[0],self.damage[1])
            else :
                self.canattack = True
                print('you can only attack every two turn with the hammer')
                return 0

class character() :
    def __init__(self,player_type:list[str,dict]=["default",data_type["default"]],player_weapon:weapon=weapon(),player_armor:armor=armor()):

        self.weapon = player_weapon
        self.armor = player_armor
        if self.weapon.name == "feast" :
            self.weapon.damage = player_type[1]["dgt_hand"]

        self.ascendence = player_type[0]

        self.total_health = player_type[1]["hp"]+player_armor.defence
        self.armor_health = player_armor.defence

        self.agility = player_type[1]["agility"]
        self.attack_order = player_type[1]["attack_order"]
 

        if player_type[0] == "archer" :
            self.arrow_count = player_type[1]["arrow_count"]
        if player_type[0] == "magician" :
            self.mana_count = player_type[1]["mana_count"]

    def getPlayerInfo(self)->None :
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
        return self.total_health <=0

    def damage(self)->int :
        if not(self.is_alive()) :
            return self.weapon.attack()
    
    def get_health_down(self,amount)->int :
        miss = rdt(0,100)
        if miss > self.agility :
            if self.total_health-amount <= 0:
                self.total_health=0
                return self.total_health
            elif not(self.armor.is_broke()):
                self.total_health -= amount
                self.armor.get_hit(amount)
                return self.total_health
            else :
                self.total_health -= amount
                return self.total_health

    
if __name__ == "__main__" :
    weapon_one = weapon(["forest_bow",data_weapon["forest_bow"]])
    armor_one = armor(["archer_armor",data_armor["archer_armor"]])
    player = character(["archer",data_type["archer"]],weapon_one,armor_one)
    player2 = character()

    player.getPlayerInfo()
    player2.getPlayerInfo()