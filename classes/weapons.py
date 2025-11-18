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

class Weapon :
    def __init__(self,player_weapon:list[str,dict]=["none",{}],player_spells:list=[["fire_ball",data_spells["fire_ball"]],["white_out",data_spells["white_out"]]]):

        if player_weapon[0] != "none" :
            self.spells = player_spells
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
    
    def choose_spell(self,spells) :
        input_message = ''
        for i in range(len(spells)) :
            input_message += f'{i}:{spells[i]}, '

        input_user = input(input_message+'which spell do you want to use ? : ')
        for char in input_user :
            if char not in ['1','2','3','4','5','6','7','8','9','0'] :
                print('wrong input')
                input()
                self.choose_spell()
        if input_user == '' :
            print('you must enter a value')
            input()
            self.choose_spell()

        if int(input_user) <= len(spells) :
            return int(input_user)
        else:
            print('must be a specified number')
            input()
            self.choose_spell()
        

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
            list_spells = [spell[0] for spell in self.spells]
            choice_spell = self.choose_spell(list_spells)
            return rdt(self.spells[choice_spell][1]["damage"][0],self.spells[choice_spell][1]["damage"][1]),self.spells[choice_spell][1]["mana_cost"]
