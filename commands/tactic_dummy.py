import math
from commands.graph import Graph
from commands.city import City
from commands.metropolis import Metropolis
from commands.general_commands import flow
from commands.general_commands import are_neighbours

def tactic_dummy(player, metropoles, cities, routes, imp1, h1, imp2, h2):

    # rename players
    enemy_player = 1 if player == 2 else 2
    imp = imp1 if player == 1 else imp2
    enemy_imp = imp2 if player == 1 else imp1
    harvest = h1 if player == 1 else h2
    enemy_harvest = h2 if player == 1 else h1

    attack = []
    for city_name, city in imp.items():
        city_army = city.get_armies()
        attacking_force = city_army - 1

        # list of of neighbouring enemy cities
        neighbour_enemy_cities = {}
        for enemy_city in cities.keys():
            if enemy_city not in imp.keys() and are_neighbours(city_name, enemy_city, routes):
                neighbour_enemy_cities.add(enemy_city)

        for enemy_city in neighbour_enemy_cities:
            j = math.ceil(attacking_force * (1/float(len(neighbour_enemy_cities))))
            x.remove(enemy_city)
            if j > 0:
                attack.append([city_name,enemy_city,j])
            attacking_force -= j
            if attacking_force <= 0:
                break
    return attack
