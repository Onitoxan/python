from src.constants import *
from random import randint


class Battle:

    def __init__(self, team_pokemon1, team_pokemon2):

        self.team_pokemon1 = team_pokemon1
        self.team_pokemon2 = team_pokemon2
        self.pokemon1 = team_pokemon1.pokemon_team[0]
        self.pokemon2 = team_pokemon2.pokemon_team[0]

        self.actual_turn = 0

    def all_dead(self, pokemon_team):
        res = False
        counter = 0
        for pokemon in pokemon_team.pokemon_team:
            if pokemon.current_hp <= 0:
                counter +=1
        if counter == len(pokemon_team.pokemon_team):
            res = True

        return res


    def is_finished(self):
        finished = (self.pokemon1.current_hp <= 0 and self.all_dead(self.team_pokemon1)) or (self.pokemon2.current_hp <= 0 and self.all_dead(self.team_pokemon2))
        if finished:
            self.print_winner()
        return finished

    def execute_turn(self, turn):
        command1 = turn.command1
        command2 = turn.command2
        attack1 = None
        attack2 = None
        if DO_ATTACK in command1.action.keys():
            attack1 = self.pokemon1.attacks[command1.action[DO_ATTACK]]
        if DO_ATTACK in command2.action.keys():
            attack2 = self.pokemon2.attacks[command2.action[DO_ATTACK]]
        if SWAP in command1.action.keys():
            attack1 = Attack("None","None",PHYSICAL,0,0,0)
            self.team_pokemon1.change_pokemon(self)

        if SWAP in command2.action.keys():
            attack2 = Attack("None","None",PHYSICAL,0,0,0)
            self.team_pokemon2.change_pokemon(self)


        # Damage formula

        self.pokemon2.current_hp -= attack1.attack_formula(self.pokemon1, self.pokemon2, attack1)
        self.pokemon1.current_hp -= attack2.attack_formula(self.pokemon2, self.pokemon1, attack2)

        self.actual_turn += 1

    def print_winner(self):
        if self.pokemon1.current_hp <= 0 < self.pokemon2.current_hp and self.all_dead(self.team_pokemon1):
            print('The winner is ' + self.pokemon2.name + ' team!')
        elif self.pokemon2.current_hp <= 0 < self.pokemon1.current_hp and self.all_dead(self.team_pokemon2):
            print('The winner is ' + self.pokemon1.name + ' team!')
        else:
            print("It's a draw!")

    def print_current_status(self):

        print(self.pokemon1.name + ' has ' + str(self.pokemon1.current_hp) + ' hp left!')
        print(self.pokemon2.name + ' has ' + str(self.pokemon2.current_hp) + ' hp left!')


class Poketeam:
    '''

    This class will allow us to have a Pokemon team of 6 Pokemons, the first pokemon in this team is the pokemon that will
    fight first.

    Conditions:     - If Pokemon1 == dead, pokemon2 enters in the battle,
                    - When all pokemons are dead, battle == end
                    -(Will add later the function of changing of pokemons in the middle of the battle)
                    - In main.py, you introduce in a tuple the name of the 6 pokemons you want in ur team, if there
                      there are more than 6 pokemons selected, ask the player what pokemon he doesn't want to choose,
                      if he chose more than 10, make him repick pokemons.
                    - The user can choose between 1 and 6 pokemons, if it is 0, make him choose one.

    '''

    def __init__(self,pokemon_team):
        if len(pokemon_team)<=6:
            self.pokemon_team = pokemon_team
            self.index_changed_to = 0
        else:
            raise ValueError("Invalid team length")


    def change_pokemon(self, battle):

        available_pokemons = [(pokemon.name,"Indice : {}".format(i))for i, pokemon in enumerate(self.pokemon_team) if pokemon.current_hp>0]



        index = int(input("Available Pokemons, select index to change {}".format(available_pokemons)))



        if not (self.pokemon_team[index].current_hp <= 0):
            swapping = self.pokemon_team[0]
            self.pokemon_team[0] = self.pokemon_team[index]
            self.pokemon_team[index] = swapping
            self.index_changed_to = index
            if battle.team_pokemon1.pokemon_team[0] == self.pokemon_team[0]:
                battle.pokemon1 = self.pokemon_team[0]
            else:
                battle.pokemon2 = self.pokemon_team[0]








class Pokemon:

    def __init__(self, name, lvl, type1, type2):
        self.name = name
        self.lvl = lvl
        self.type1 = type1
        self.type2 = type2
        self.attacks = []
        self.stats = {}
        self.current_status = 0
        self.current_hp = 0



class Attack:

    def __init__(self, name, element, category, pp, power, accuracy):
        self.name = name
        self.element = element
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.attackformula = 0

    def recorre_diccionario(self, atacante, defensor, diccionario):

        lista = [[[value1 for key1, value1 in value.items() if key1 == defensor] for key, value in dicc.items() if
                  key == atacante] for dicc in diccionario]

        res = 0

        if lista[0][0] != 0:
            res += lista[0][0][0]
        else:
            exit(NotImplementedError)

        return res

    def attack_formula(self, pokemon_attacking, pokemon_defending, attack):

        self.attackformula_physical = int(((((2 * pokemon_attacking.lvl) / 5) + 2) * attack.power * (
                pokemon_attacking.stats.get(ATTACK, 1) / pokemon_defending.stats.get(DEFENSE, 1)) + 2) / 50)

        self.attackformula_special = int(((((2 * pokemon_attacking.lvl) / 5) + 2) * attack.power * (
                pokemon_attacking.stats.get(SPATTACK, 1) / pokemon_defending.stats.get(SPDEFENSE, 1)) + 2) / 50)

        random_factor = int(round(randint(217, 255) / 255))
        type_attack_pokemon = 1
        type_efective_pokemon = 1
        type_not_efective_pokemon = 1  # create pokemon's type chart using this format -->   {str:{[str,str...]: int}}

        critical_chance1 = randint(0, 255)
        critical_chance2 = randint(0, 255)

        if pokemon_attacking.type1 == attack.element or pokemon_attacking.type2 == attack.element:

            type_attack_pokemon *= 1.5
        elif pokemon_attacking.type1 != attack.element or pokemon_attacking.type2 != attack.element:

            type_attack_pokemon *= 1

        if attack.category == PHYSICAL:

            if critical_chance1 < critical_chance2:
                return self.attackformula_physical * 2
            else:
                return int(round(self.attackformula_physical * random_factor * type_attack_pokemon))

        elif attack.category == SPECIAL:

            if critical_chance1 < critical_chance2:
                return self.attackformula_special * 2
            else:
                return int(round(self.attackformula_special * random_factor * type_attack_pokemon))
        else:
            raise NotImplementedError('Error in attack_formula')


class Turn:



    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):
        return self.command1 is not None and self.command2 is not None


class Command:

    def __init__(self, action):
        self.action = action

