import math
from commands.graph import Graph
from commands.city import City
from commands.metropolis import Metropolis
from commands.general_commands import flow
from commands.general_commands import are_neighbours

def tactic(player, metropoles, cities, routes, imp1, h1, imp2, h2):

    # rename players
    enemy_player = 1 if player == 2 else 2
    imp = imp1 if player == 1 else imp2
    enemy_imp = imp2 if player == 1 else imp1
    harvest = h1 if player == 1 else h2
    enemy_harvest = h2 if player == 1 else h1

    #calculate score for every enemy city
    enemy_cities_scores = {}
    for enemy_city in cities.keys(): #I have to consider cities that are not in the enemy imperium nor in mine
        if not cities[enemy_city].is_metropolis() and enemy_city not in imp:
            a = flow(player, metropoles, cities, routes, imp.copy(), None, None) # calculate flow from imp1 city to my metropolis
            b = flow(player, metropoles, cities, routes, imp.copy(), enemy_city, None) # calculate flow from imp1 plus enemy city to my metropolis
            c = b-a
            d = flow(enemy_player, metropoles, cities, routes, enemy_imp.copy(), None, None) # calculate flow from imp2 city to enemy metropolis
            e = flow(enemy_player, metropoles, cities, routes, enemy_imp.copy(), None, enemy_city) # calculate flow from imp2 minus enemy city to enemy metropolis
            f = d-e

            i = c + f # how valuable is enemy_city
            enemy_cities_scores[enemy_city] = i

    attack = []
    for city_name, city in imp.items():
        city_army = city.get_armies()
        attacking_force = city_army - 1

        # total score of neighbouring enemy cities
        x = 0
        for enemy_city in cities.keys():
            if enemy_city in enemy_cities_scores and are_neighbours(city_name, enemy_city, routes):
                x += enemy_cities_scores[enemy_city]

        list_of_sorted_neighbour_enemy_cities = []
        for enemy_city in cities.keys():
            if enemy_city in enemy_cities_scores and are_neighbours(city_name, enemy_city, routes):
                list_of_sorted_neighbour_enemy_cities.append(enemy_city)

        list_of_sorted_neighbour_enemy_cities.sort(key=lambda x: enemy_cities_scores[x], reverse=True)

        for enemy_city in list_of_sorted_neighbour_enemy_cities:
            j = math.ceil(attacking_force * (enemy_cities_scores[enemy_city]/float(x)))
            x -= enemy_cities_scores[enemy_city]
            if j > 0:
                attack.append([city_name,enemy_city,j])
            attacking_force -= j
            if attacking_force <= 0:
                break
    return attack
