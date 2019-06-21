# -*encoding=utf-8*-
# from constants import * Imported from scanner
# from models import *  Imported from scanner
from src.scanner_pokemons import *
from copy import deepcopy

# Define pokemons with its stats
def main():

    file = './data/Pokemon.csv'
    data = read_csv(file)
    data_filtered_pokemon_info = filtre_pokemon_class_info(data)
    data_filtered_stat_info = filtre_pokemon_stat_info(data)
    Dataset = create_pokemon_data(data_filtered_pokemon_info, data_filtered_stat_info)




    data_pokemon_11 = Dataset.get('Mew', 'ERROR')
    data_pokemon_12 = Dataset.get('Blastoise', 'ERROR')
    data_pokemon_13 = Dataset.get('Mew', 'ERROR')
    data_pokemon_14 = Dataset.get('Mew', 'ERROR')
    data_pokemon_15 = Dataset.get('Weedle', 'ERROR')
    data_pokemon_16 = Dataset.get('Charizard', 'ERROR')


    data_pokemon_21 = Dataset.get('Gyarados', 'ERROR')
    data_pokemon_22 = Dataset.get('Lapras', 'ERROR')
    data_pokemon_23 = Dataset.get('Pinsir', 'ERROR')
    data_pokemon_24 = Dataset.get('Vaporeon', 'ERROR')
    data_pokemon_25 = Dataset.get('Jolteon', 'ERROR')
    data_pokemon_26 = Dataset.get('Mewtwo', 'ERROR')

    pokemon_team1 = Poketeam([])   #Implementar todavia (En estado de testeo)
    pokemon_team2 = Poketeam([])   #Implementar todavia


    pokemon11 = data_pokemon_11[0]
    pokemon12 = data_pokemon_12[0]
    pokemon13 = deepcopy(data_pokemon_13[0])
    pokemon14 = deepcopy(data_pokemon_14[0])
    pokemon15 = data_pokemon_15[0]
    pokemon16 = data_pokemon_16[0]

    pokemon21 = data_pokemon_21[0]
    pokemon22 = data_pokemon_22[0]
    pokemon23 = data_pokemon_23[0]
    pokemon24 = data_pokemon_24[0]
    pokemon25 = data_pokemon_25[0]
    pokemon26 = data_pokemon_26[0]


    pokemon11.current_hp = data_pokemon_11[1].get(HP)
    pokemon12.current_hp = data_pokemon_12[1].get(HP)
    pokemon13.current_hp = data_pokemon_13[1].get(HP)
    pokemon14.current_hp = data_pokemon_14[1].get(HP)
    pokemon15.current_hp = data_pokemon_15[1].get(HP)
    pokemon16.current_hp = data_pokemon_16[1].get(HP)

    pokemon21.current_hp = data_pokemon_21[1].get(HP)
    pokemon22.current_hp = data_pokemon_22[1].get(HP)
    pokemon23.current_hp = data_pokemon_23[1].get(HP)
    pokemon24.current_hp = data_pokemon_24[1].get(HP)
    pokemon25.current_hp = data_pokemon_25[1].get(HP)
    pokemon26.current_hp = data_pokemon_26[1].get(HP)

    # Define the stats

    pokemon11.stats = data_pokemon_11[1]
    pokemon12.stats = data_pokemon_12[1]
    pokemon13.stats = data_pokemon_13[1]
    pokemon14.stats = data_pokemon_14[1]
    pokemon15.stats = data_pokemon_15[1]
    pokemon16.stats = data_pokemon_16[1]


    pokemon21.stats = data_pokemon_21[1]
    pokemon22.stats = data_pokemon_22[1]
    pokemon23.stats = data_pokemon_23[1]
    pokemon24.stats = data_pokemon_24[1]
    pokemon25.stats = data_pokemon_25[1]
    pokemon26.stats = data_pokemon_26[1]

    # Attacks

    pokemon11.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100),
                        Attack('random attack', 'normal', SPECIAL, 35, 20, 100)]
    pokemon12.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100),
                        Attack('random attack', 'normal', SPECIAL, 35, 20, 100)]
    pokemon13.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100),
                        Attack('random attack', 'normal', SPECIAL, 35, 20, 100)]
    pokemon14.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100),
                        Attack('random attack', 'normal', SPECIAL, 35, 20, 100)]
    pokemon15.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100),
                        Attack('random attack', 'normal', SPECIAL, 35, 20, 100)]
    pokemon16.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100),
                        Attack('random attack', 'normal', SPECIAL, 35, 20, 100)]



    pokemon21.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 50, 100)]
    pokemon22.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100)]
    pokemon23.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100)]
    pokemon24.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100)]
    pokemon25.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100)]
    pokemon26.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 10, 100)]


    # Add Pokemons to Pokemon Team

    pokemon_team1.pokemon_team.append(pokemon11)
    pokemon_team1.pokemon_team.append(pokemon12)
    pokemon_team1.pokemon_team.append(pokemon13)
    pokemon_team1.pokemon_team.append(pokemon14)
    pokemon_team1.pokemon_team.append(pokemon15)
    pokemon_team1.pokemon_team.append(pokemon16)

    pokemon_team2.pokemon_team.append(pokemon21)
    pokemon_team2.pokemon_team.append(pokemon22)
    pokemon_team2.pokemon_team.append(pokemon23)
    pokemon_team2.pokemon_team.append(pokemon24)
    pokemon_team2.pokemon_team.append(pokemon25)
    pokemon_team2.pokemon_team.append(pokemon26)




    # Start Battle

    battle = Battle(pokemon_team1, pokemon_team2)

    def ask_command(pokemon, pokemon_team):
        command = None
        if pokemon.current_hp <= 0 and not battle.all_dead(pokemon_team):
            pokemon_team.change_pokemon(battle)
            if(pokemon_team.pokemon_team[pokemon_team.index_changed_to].current_hp <= 0 and battle.pokemon1.name == pokemon_team.pokemon_team[pokemon_team.index_changed_to].name ):        #Funciona pero hay que limpiarlo
                battle.pokemon1 = pokemon_team.pokemon_team[0]
                command = Command({SWAP:1})
            else:
                battle.pokemon2 = pokemon_team.pokemon_team[0]
                command = Command({SWAP:1})

        else:
            while not command:
                # DO_ATTACK -> attack 0

                tmp_command = input('What should ' + pokemon.name + ' do?').split(' ')
                if len(tmp_command) == 2:
                    try:
                        if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                            command = Command({DO_ATTACK: int(tmp_command[1])})
                    except Exception:
                        pass
                elif len(tmp_command) == 1:
                    if tmp_command[0] == SWAP:
                        command = Command({SWAP: 0})
        return command

    while not battle.is_finished():
        # Ask the trainers for the command they want to do

        command1 = ask_command(pokemon_team1.pokemon_team[0],pokemon_team1)
        command2 = ask_command(pokemon_team2.pokemon_team[0],pokemon_team2)



        turn = Turn()
        turn.command1 = command1
        turn.command2 = command2



        if turn.can_start():
            # execute turn
            battle.execute_turn(turn)
            battle.print_current_status()


if __name__ == '__main__':
    main()
