from classes.player import Character
import json

with open("data/ascendance.json","r",encoding='utf-8') as f :
    data_type = json.load(f)

with open("data/weapons.json","r",encoding='utf-8') as f :
    data_weapon = json.load(f)

with open("data/armors.json","r",encoding='utf-8') as f :
    data_armor = json.load(f)

class Arena :
    def __init__(self,player_1:Character,player_2:Character):
        self.players = [player_1,player_2]
        self.win = False

    def check_player_dies(self)->Character:
        for player in self.players :
            if not(player.is_alive()) :
                self.players.remove(player)
                self.win = True
                return self.players[0]