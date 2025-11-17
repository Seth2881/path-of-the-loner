from random import randint as rdt
import json

with open("../data/player/ascendance.json","r",encoding='utf-8') as f :
    data_monsters = json.load(f).items()
    for ele in data_monsters :
        data_monsters.index(ele) = [ele[0],ele[1]]

class monster :
    def __init__(self):
        pass