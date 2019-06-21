# Create pokemon's type chart
import csv
import re
from collections import Counter
from functools import reduce
#Necesito obtener un log de forma {(str,str):{str:int}}

def read_type_chart(file):
    regexp = r'"(?P<defend_type1>\w+)\s+(?P<defend_type2>\w+)\s+(?P<PKMN>\d+(\d)?)\s+(?P<normal>\d+(\.\d+)?)\s+(?P<fire>\d+(\.\d+)?)\s+(?P<water>\d+(\.\d+)?)\s+(?P<electric>\d+(\.\d+)?)\s+(?P<grass>\d+(\.\d+)?)\s+(?P<ice>\d+(\.\d+)?)\s+(?P<fighting>\d+(\.\d+)?)\s+(?P<poison>\d+(\.\d+)?)\s+(?P<ground>\d+(\.\d+)?)\s+(?P<flying>\d+(\.\d+)?)\s+(?P<psychic>\d+(\.\d+)?)\s+(?P<bug>\d+(\.\d+)?)\s+(?P<rock>\d+(\.\d+)?)\s+(?P<ghost>\d+(\.\d+)?)\s+(?P<dragon>\d+(\.\d+)?)\s+(?P<dark>\d+(\.\d+)?)\s+(?P<steel>\d+(\.\d+)?)\s+(?P<fairy>\d+(\.\d+)?)"'


    with open(file, encoding='utf8', mode='r') as f:

        log=[]
        for line in f:
            # Aplicamos la expresión regular sobre cada línea
            matches = re.match(regexp, line)
            if matches:  # Si se encuentran coincidencias para los patrones
                defend_type1 = matches.group('defend_type1')
                defend_type2 = matches.group('defend_type2')
                #PKMN = matches.group('PKMN')
                normal = matches.group('normal')
                fire = matches.group('fire')
                water = matches.group('water')
                electric = matches.group('electric')
                grass = matches.group('grass')
                ice = matches.group('ice')
                fighting = matches.group('fighting')
                poison = matches.group('poison')
                ground = matches.group('ground')
                flying = matches.group('flying')
                psychic = matches.group('psychic')
                bug = matches.group('bug')
                rock = matches.group('rock')
                ghost = matches.group('ghost')
                dragon = matches.group('dragon')
                dark = matches.group('dark')
                steel = matches.group('steel')
                fairy = matches.group('fairy')

                dicc = {(defend_type1,defend_type2): {'normal': normal,
                            'fire': fire, 'water': water, 'electric': electric, 'grass': grass, 'ice': ice,
                            'fighting': fighting, 'poison': poison, 'ground': ground, 'flying': flying,
                            'psychic': psychic, 'bug': bug, 'rock': rock, 'ghost': ghost, 'dragon': dragon,
                            'dark': dark, 'steel': steel, 'fairy': fairy}}

                log.append(dicc)

        return log



    
