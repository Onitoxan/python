#----------------------SCANNER TST-------------------------
'''
file = './data/Pokemon.csv'

data = read_csv(file)

#print(data)
data1 = filtre_pokemon_class_info(data)
data2 = filtre_pokemon_stat_info(data)
print(create_pokemon_data(data1, data2))

'''
'''
#-----------------------------------------------------------

#-----------------------MAIN TST-----------------------------
# Defining scanner constants
file = './Pokemon.csv'
data = read_csv(file)
data_filtered_pokemon_info = filtre_pokemon_class_info(data)
data_filtered_stat_info = filtre_pokemon_stat_info(data)
Dataset = create_pokemon_data(data_filtered_pokemon_info, data_filtered_stat_info)

print(data_filtered_stat_info)

#-----------------------DEBUGGING ZONE-----------------------
'''
'''
#from models, in Attack class

def attack_formula(self, pokemon1, pokemon2, attack):

    random_factor = int(round(randint(217,255)/255))
    type_attack_pokemon1 = 0
    type_attack_pokemon2 = 0

    critical_chance1 = randint(0,255)
    critical_chance2 = randint(0,255)

    if pokemon1.type1 == self.element or pokemon1.type2 == self.element:
        type_attack_pokemon1 = 1.5
        return type_attack_pokemon1
    elif pokemon1.type1 != self.element or pokemon1.type2 != self.element:
        type_attack_pokemon1 = 1
        return type_attack_pokemon1

    elif pokemon2.type1 == self.element or pokemon2.type2 == self.element:
        type_attack_pokemon2 = 1.5
        return type_attack_pokemon2

    elif pokemon1.type1 != self.element or pokemon1.type2 != self.element:
        type_attack_pokemon2 = 1
        return type_attack_pokemon2

#Revisar el resto de esta funcion porque hay algo que hace que me de 1 como return de attackformula(hacia abajo)
    else:
        if self.category == PHYSICAL:
            self.attackformula = int(((((2 * pokemon1.lvl) / 5) + 2) * attack.power * (
                    pokemon1.stats.get(ATTACK, 1) / pokemon2.stats.get(DEFENSE, 1)) + 2) / 50)
            if critical_chance1 < critical_chance2:
                return self.attackformula * 2
            else:
                return int(round(self.attackformula * random_factor * type_attack_pokemon1))

        elif self.category == SPECIAL:
            self.attackformula = int(((((2 * pokemon1.lvl) / 5) + 2) * attack.power * (
                    pokemon1.stats.get(SPATTACK, 1) / pokemon2.stats.get(SPDEFENSE, 1)) + 2) / 50)

            if critical_chance1 < critical_chance2:
                return self.attackformula * 2
            else:
                return int(round(self.attackformula * random_factor * type_attack_pokemon1))


        if self.category == PHYSICAL:
            self.attackformula = int(((((2 * pokemon2.lvl) / 5) + 2) * attack.power * (
                    pokemon2.stats.get(ATTACK, 1) / pokemon1.stats.get(DEFENSE, 1)) + 2) / 50)
            if critical_chance1 < critical_chance2:
                return self.attackformula * 2
            else:
                return int(round(self.attackformula * random_factor * type_attack_pokemon2))

        elif self.category == SPECIAL:
            self.attackformula = int(((((2 * pokemon2.lvl) / 5) + 2) * attack.power * (
                    pokemon2.stats.get(SPATTACK, 1) / pokemon1.stats.get(SPDEFENSE, 1)) + 2) / 50)

            if critical_chance1 < critical_chance2:
                return self.attackformula * 2
            else:
                return int(round(self.attackformula * random_factor * type_attack_pokemon2))
        else:
            raise ('Error in attack_formula')

'''
#-------------------------------Regular expression test----------------------------------------------
'''

def prueba_ER(expresion_regular):
    print('Probando la ER "' + expresion_regular + '"')
    cadena = input("Introduce una cadena:")
    if re.fullmatch(expresion_regular, cadena):
        print('La cadena ENCAJA en el patrón.')
    else:
        print('La cadena NO ENCAJA en el patrón.')

prueba_ER(r'"(?P<defend_type1>\w+)\s+(?P<defend_type2>\w+)\s+(?P<PKMN>\d+(\d)?)\s+(?P<normal>\d+(\.\d+)?)\s+(?P<fire>\d+(\.\d+)?)\s+(?P<water>\d+(\.\d+)?)\s+(?P<electric>\d+(\.\d+)?)\s+(?P<grass>\d+(\.\d+)?)\s+(?P<ice>\d+(\.\d+)?)\s+(?P<fighting>\d+(\.\d+)?)\s+(?P<poison>\d+(\.\d+)?)\s+(?P<ground>\d+(\.\d+)?)\s+(?P<flying>\d+(\.\d+)?)\s+(?P<psychic>\d+(\.\d+)?)\s+(?P<bug>\d+(\.\d+)?)\s+(?P<rock>\d+(\.\d+)?)\s+(?P<ghost>\d+(\.\d+)?)\s+(?P<dragon>\d+(\.\d+)?)\s+(?P<dark>\d+(\.\d+)?)\s+(?P<steel>\d+(\.\d+)?)\s+(?P<fairy>\d+(\.\d+)?)"')

'''

#print(read_type_chart('./data/type_chart.txt'))

#------------------------------------reading attack files-----------------
'''

def read_attacks(file,attack):
    lista = []
    with open(file, encoding="utf-8") as f:

        for linea in f:
            listahehe = linea.split(";")
            nombre = listahehe[0].strip("\ufeff")
            tipo = listahehe[1]
            power = int(listahehe[2])
            accuracy = int(listahehe[3])
            pp = int(listahehe[4])

            lista.append({nombre:(tipo,power,accuracy,pp)})

    diccionario= {}
    for x in lista:
        diccionario
    print(diccionario)
eo = read_attacks("./data/ataques.csv", "Bite")

'''