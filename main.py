from random import randint as rdt, choice
from classes.player import Armor, Weapon, Character
from classes.monster import Monster
from classes.rooms import Room
from classes.arena import Arena
import json

with open("data/spells.json","r",encoding='utf-8') as f:
    data_spells = json.load(f)
with open("data/ascendance.json","r",encoding='utf-8') as f :
    data_ascendance = json.load(f)
with open("data/weapons.json","r",encoding='utf-8') as f :
    data_weapon = json.load(f)
with open("data/armors.json","r",encoding='utf-8') as f :
    data_armor = json.load(f)
with open("data/monsters.json","r",encoding='utf-8') as f :
    data_monsters = json.load(f)

monster_common = [[monster,value] for monster,value in data_monsters.items() if value["type"] == "normal"]
monster_elite = [[monster,value] for monster,value in data_monsters.items() if value["type"] == "elite"]
bosses = [[monster,value] for monster,value in data_monsters.items() if value["type"] == "boss" and value["name"] != "Soron, lord of The Ring"]
soron = ["soron",data_monsters["soron"]]

weapons = [weapon for weapon in data_weapon]
armors = [armor for armor in data_armor]
ascendances = [ascendance for ascendance in data_ascendance]

#FUNCTION

def show_info(dico):
    for key,value in dico.items() :
        print(f'{key} : {value}')

def pvp_or_pve() :
    a = input('pvp (1) ou pve (2) ? : ')
    if a not in ['1','2']:
        print('please use 1 or 2 as an answer, blank input are pohibited.')
        pvp_or_pve()
    else :
        return a
    
def show_or_choose(choices,item_type) :
    global data_armor
    global data_ascendance
    global data_weapon

    input_choice = ''
    for i in range(len(choices)) :
        input_choice += f'{i+1}:{choices[i]}, '
    input_choice+=f'0;(number beetwen {1} and {len(choices)}):show specificity : '
    
    answer = input(input_choice)

    if answer not in [f'0;{i+1}' for i in range(len(choices))] :
        if answer not in [f'{i+1}' for i in range(len(choices))] :
            print('syntax error')
            input()
            show_or_choose(choices,item_type)
    
    if answer in [f'0;{i+1}' for i in range(len(choices))] :
        show_info((data_armor[choices[int(answer[2:])-1]] if item_type == 'armor' else (data_weapon[choices[int(answer[2:])-1]] if item_type == 'weapon' else data_ascendance[choices[int(answer[2:])-1]])))
        input()
        return None
    elif int(answer) <= len(choices)+1 :
        input(f'vous avez choisi {choices[int(answer)-1]}.')
        print()
        return choices[int(answer)-1]
    else :
        print('number too high')
        input()
        show_or_choose(choices,item_type)


def choose_w_a_or_ascend() :
    w_a_or_ascend = input('1:weapons, 2:armors, 3:ascendace, 0:exit : ')
    if w_a_or_ascend not in ['0','1','2','3']:
        print('please specify 0,1,2 or 3, not anything else')
        choose_w_a_or_ascend()
    else :
        return w_a_or_ascend

def build_your_character(weapons,armors,ascendances):
    #possibilité de voir les différentes caractéristique d'une ascendance, d'une arme ou d'une armure
    #possibilité de choix facilitée par une nombre associé à chaque armure, weapon et ascendance
    #choix dans l'ordre que veux le joueur
    hero_name = input('what is your hero name? : ')
    weapon = []
    armor = None
    ascendance = None
    
    number_choices = 0
    while number_choices < 4 :
        choice = choose_w_a_or_ascend()
        if choice == '0' :
            return [hero_name]

        if choice == '1' and len(weapon)<2 :
            weapon.append(show_or_choose(weapons,'weapon'))
            if len(weapon) != 0:
                number_choices += 1
        else :
            print('weapon already chosen')

        if choice == '2' and armor == None:
            armor = show_or_choose(armors,'armor')
            if armor != None :
                number_choices += 1
        else :
            print('armor already chosen')
            
        if choice == '3' and ascendance == None:
            ascendance = show_or_choose(ascendances,'ascendance')
            if ascendance != None :
                number_choices += 1
        else :
            print('ascendace already chosen')

    return [hero_name,ascendance,weapon,armor]

def which_ennemy(ennemy_dict:dict):
    which = input(str(ennemy_dict)[1:-1]+' which monster do you want to hit ? : ')
    if which not in [str(i) for i in range(len([value for _,value in ennemy_dict]))] or which == '':
        print('please use a number displayed in the input prompt')
        which_ennemy(ennemy_dict)
    else :
        return which

#PRINCIPAL PROGRAM

choice_player_1 = build_your_character(weapons,armors,ascendances)

if len(choice_player_1) >=3 :
    if len(choice_player_1[2]) == 1 :
        player_1 = Character([choice_player_1[0],data_ascendance[choice_player_1[1]]],Weapon([choice_player_1[2][0],data_weapon[choice_player_1[2][0]]]),Armor([choice_player_1[3],data_armor[choice_player_1[3]]]))
    else :
        player_1 = Character([choice_player_1[0],data_ascendance[choice_player_1[1]]],[Weapon([choice_player_1[2][0],data_weapon[choice_player_1[2][0]]]),Weapon([choice_player_1[2][1],data_weapon[choice_player_1[2][1]]])],Armor([choice_player_1[3],data_armor[choice_player_1[3]]]))
else :
    player_1 = Character()

player_1.get_player_info()

pvp_pve = pvp_or_pve()
print(pvp_pve)

if pvp_pve == '1' :


    ascendance_choice = choice(ascendances)
    weapon_choice = choice(weapons)
    armors_choice = choice(armors)

    bot = Character([ascendance_choice,data_ascendance[ascendance_choice]],Weapon([weapon_choice,data_weapon[weapon_choice]]),Armor([armors_choice,data_armor[armors_choice]]))

    arena = Arena(player_1,bot)

    bot.get_player_info()
    input()
    print("----------------------")
    print()
    print("     BIENVENUE EN     ")
    print("       MODE PVP       ")
    print()
    input()
    print("     LET'S FIGHT!     ")
    input()

    while arena.check_player_dies() is None :
        if bot.attack_order == 1 and player_1.attack_order != 1:
            damage_2 = player_1.get_health_down(bot.damage())
            damage_1 = bot.get_health_down(player_1.damage())
        elif player_1.attack_order == 1 and bot.attack_order != 1:
            damage_1 = bot.get_health_down(player_1.damage())
            damage_2 = player_1.get_health_down(bot.damage())
        else :
            choose_who_hit_first = choice([player_1,bot])
            if choose_who_hit_first == player_1 :
                damage_2 = player_1.get_health_down(bot.damage())
                damage_1 = bot.get_health_down(player_1.damage())
            else :
                damage_1 = bot.get_health_down(player_1.damage())
                damage_2 = player_1.get_health_down(bot.damage())

        if damage_1[0] != 'missed' :
            print(f'You dealed {damage_1[0]} damage to {bot}')
        else :
            print(f'{bot} as dogged your attack !')

        if damage_2[0] == 'missed' :
            print(f"you dogged {bot}'s attack !")
        else :
            print(f'{bot} dealed {damage_2[0]} to you')

        input()
        if bot.total_health <= 0 or player_1.total_health:
            print(f'{bot} have {bot.total_health}/{bot.total_health_max}HP')
            print(f'You have {player_1.total_health}/{player_1.total_health_max}HP')
            input()

        if arena.check_player_dies() != None:
            if player_1.total_health == 0 :
                print("\nYou have been defeated in combat...")
                print("GAME OVER")
                exit()
            else :
                print("\n" + "="*70)
                print(f"       CONGRATULATIONS! YOU HAVE WON AGAINST THE {str(bot.name).upper()}!")
                print(f"       Hero: {player_1.name}")
                print(f"       Final HP: {player_1.total_health}/{player_1.total_health_max}")
                print("       YOU ARE VICTORIOUS!")
                print("="*70)
                exit()

else :
    rooms = [Room(1),Room(2),Room(3)]

    room_nbr = 0

    while room_nbr <4 :
        actual_room = rooms[room_nbr].monsters
        ennemy = [f'{monster.name} the {monster.race} ({monster.type})' for monster in rooms[room_nbr].monsters]
        print(ennemy)
        input()
        while len(ennemy) > 0:
            order = []
            ennemy_number = {str(i):ennemy[i] for i in range(len(ennemy))}
            nbr = int(which_ennemy(ennemy_number))

            if player_1.attack_order == 1 :
                dmg = actual_room[nbr].get_hit(player_1.damage())
                print(f'you deal {dmg} to {actual_room[nbr]}')
                for mob in actual_room :
                    dmg = player_1.get_hit(mob.damage())
                    print(f'{mob} deals you {dmg}')
            else :
                while len(order) != len(actual_room)+1 :
                    order_choice = choice(actual_room+[player_1])
                    if order_choice not in order :
                        order.append(order_choice)
                print(order)
                input()
                
                for mob in order :
                    if type(mob) == Monster :
                        dmg = player_1.get_health_down(mob.damage())
                        print(f'{mob} deals you {dmg}')
                    elif type(mob) == Character :
                        dmg = actual_room[nbr].get_hit(player_1.damage())
                        print(f'you deal {dmg} to {actual_room[nbr].name} the {actual_room[nbr].race} ({actual_room[nbr].type})')

            rooms[room_nbr].check_monsters_dies()