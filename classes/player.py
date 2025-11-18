from random import randint as rdt
import json
from classes.weapons import Weapon
from classes.armors import Armor

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

class Character() :
    def __init__(self,player_type:list[str,dict]=["default",data_type["default"]],player_weapon=Weapon(),player_armor:Armor=Armor()):

        if type(player_weapon)==list :
            self.weapon = player_weapon
        else :
            self.weapon = [player_weapon]

        if self.weapon[0].name == "feast" and len(self.weapon) == 1:
            self.weapon[0].damage = player_type[1]["dgt_hand"]
        elif self.weapon[0].name == "feast" :
            self.weapon.pop(0)
        elif len(self.weapon) == 2 and self.weapon[1].name == "feast" :
            self.weapon.pop(1)
        elif len(self.weapon) == 2 and self.weapon[0].name == "feast" and self.weapon[1].name == "feast" :
            self.weapon.pop(0)
            self.weapon[0].damage = player_type[1]["dgt_hand"]

        self.armor = player_armor
        self.mana_count = 0

        self.name = player_type[0]
        self.ascendance = player_type[1]["ascend"]

        self.total_health_max =  player_type[1]["hp"]+player_armor.defence
        self.total_health = player_type[1]["hp"]+player_armor.defence
        self.armor_health = player_armor.defence

        self.agility = player_type[1]["agility"]
        self.attack_order = player_type[1]["attack_order"]
        self.nbr_attack = 1

        self.is_magical = False
        if self.ascendance == "warrior" :
            self.nbr_attack = 2
        if self.ascendance == "archer" :
            self.arrow_count = player_type[1]["arrow_count"]
        if self.ascendance == "magician" :
            self.mana_count = player_type[1]["mana_count"]
            self.is_magical = True

        self.max_mana_count = self.mana_count

    def __str__(self):
        return self.name

    def get_player_info(self)->None :
        print("character")
        input("__________________________")
        for key,value in self.__dict__.items() :
            if str(value) not in ["",'[]']:
                print(key,':',value)
        print("__________________________")
        print()
        print("weapon(s)")
        input("__________________________")
        if len(self.weapon) == 1 :
            for key,value in self.weapon[0].__dict__.items() :
                if str(value) not in ['[]']:
                    print(key,':',value)
        else :
            print('weapon 1')
            for key,value in self.weapon[0].__dict__.items() :
                if str(value) not in ['[]']:
                    print(key,':',value)
            print('weapon 2')
            for key,value in self.weapon[1].__dict__.items() :
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

    def make_choice(self,choice_list:list)->int :
        if type(choice_list) == list:
            if len(choice_list) == 2 :
                input_user = input(f'1:{choice_list[0]}, 2:{choice_list[1]} | what weapon do you want to use ? : ')
                if input_user not in ['1','2'] :
                    print('wrong input')
                    input()
                    self.make_choice(choice_list)
                return int(input_user)
            else :
                return 1
        else :
            return 1

    def damage(self)->int :
        if self.is_alive() :
            if self.ascendance == "warrior" :
                print("you have double strike")
            if len(self.weapon) == 1:
                return self.weapon[0].attack()*self.nbr_attack
            else :
                choice_list = [self.weapon[i].name for i in range(len(self.weapon))]
                choice_input = self.make_choice(choice_list)
                if self.weapon[choice_input-1].ismagical == False :
                    return self.weapon[choice_input-1].attack()*self.nbr_attack
                else :
                    attack = self.weapon[choice_input-1].attack()
                    if  self.mana_count-attack[1] == 0 or self.mana_count-attack[1] > 0:
                        print(f'your mana pool after the spell casting :')
                        input(f'{self.mana_count}/{self.max_mana_count}')
                        return attack[0]
                    else :
                        print("can't cast a spell your mana reserve is too low")
                        input()
                        self.damage()
    
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
        print(f'{self.name} as {self.total_health}HP')