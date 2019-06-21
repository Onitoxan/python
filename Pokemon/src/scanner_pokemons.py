from src.models import *
from src.constants import *
import csv

'''

We have a csv file with the following parameters:

        #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
        1  2     3       4     5    6   7       8       9      10     11       12        13
        
        int,str,str,str,int,int,int,int,int,int,int,int,int,boolean

First of all, we need to get as exit : Pokemon(name,lvl,type1,type2) and also the stats as a dictionary asociated to 
that pokemon.

As an entry we are going to have a name of a pokemon but it is not between "", we will have something like for
example Alakazam, we have to create all this constants with a for loop, to make it easier for us later to work
with pokemons even though it's hard to make now, but is worth the pain

Here we add all the pokemons from the first Generation, excluding Mega evolutions
'''


def read_csv(file):
    '''

    Read the CSV file and return a tuple of 2 lists of tuples with the datas necessaries for the pokemon
    info and also for the pokemon stats
    '''

    with open(file, encoding='utf-8') as f:
        scanner = csv.reader(f)
        next(scanner)
        # Filtres data and removes mega evolutions and we also only get gen 1 pokemons
        filtred_info_for_pokemon = [(name, type1, type2, int(hp), int(attack), int(defense), int(spattack),
                                     int(spdefense), int(speed), int(gen)) for
                                    _, name, type1, type2, _, hp, attack, defense, spattack, spdefense, speed, gen, _ in
                                    scanner
                                    if 'Mega' not in name and int(gen) == 1]

    return filtred_info_for_pokemon


def filtre_pokemon_class_info(data):
    filtred_info_for_pokemon = [(name, 100, type1, type2) for
                                name, type1, type2, _, _, _, _, _, _, gen in data
                                if 'Mega' not in name and int(gen) == 1]

    return filtred_info_for_pokemon


def filtre_pokemon_stat_info(data):
    filtred_info_for_stats = [(int(hp), int(attack), int(defense), int(spattack), int(spdefense), int(speed))
                              for name, _, _, hp, attack, defense, spattack, spdefense, speed, gen in
                              data
                              if 'Mega' not in name and int(gen) == 1]

    return filtred_info_for_stats


def create_pokemon_data(data1, data2):
    pokeinfo = {
    data[0]: (Pokemon(data[0], data[1], data[2], data[3]), {stat: data2[j][i] for i, stat in enumerate(STATS)}) for
    j, data in enumerate(data1)}
    return pokeinfo


#To use in main.py, 'Dataset' contains all the data filtered and distributed as I want

