import math
from commands.graph import Graph
from commands.city import City
from commands.metropolis import Metropolis
from commands.general_commands import get_metropolis
from commands.general_commands import flow
from commands.general_commands import are_neighbours

def safeguard_metropolis(player, metropoles, cities, routes, imp, enemy_imp, current_armies):
    metripolis = get_metropolis(metropoles, player)
    metropolis_neighbours= {}
    for city in imp.keys():
        if are_neighbours(city, metripolis, routes):
            metropolis_neighbours[city] = 0

    for city in metropolis_neighbours.keys():
        for enemy_city in enemy_imp.keys():
            if are_neighbours(city, enemy_city, routes):
                metropolis_neighbours[city] += 1

    selected_neighbour = None
    for neighbour in metropolis_neighbours.keys():
        if not selected_neighbour:
            selected_neighbour = neighbour
        if metropolis_neighbours[neighbour] < metropolis_neighbours[selected_neighbour]:
            selected_neighbour = neighbour

    temporary_imperium = []
    for city in imp.keys():
        armies = 1
        if city == selected_neighbour:
            armies += current_armies
        temporary_imperium.append([city, armies])

    return temporary_imperium

def maximize_armies_on_important_cities(player, metropoles, cities, routes, imp, enemy_imp, enemy_player,  current_armies):
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

    # add sum of neighbour enemy city scores to every city
    cities_scores = {}
    for city in imp.keys():
        # total score of neighbouring enemy cities
        j = 0
        for enemy_city in cities.keys():
            if enemy_city in enemy_cities_scores and are_neighbours(city, enemy_city, routes):
                j += enemy_cities_scores[enemy_city]
        cities_scores[city] = j

    temporary_imperium = []
    sorted_cities = list(cities_scores.keys())
    sorted_cities.sort(key=lambda x: cities_scores[x], reverse=True)
    x = sum(cities_scores.values())

    for city in sorted_cities:
        j= 0
        if current_armies > 0:
            j = math.ceil(current_armies * (cities_scores[city]/float(x)))
            x -= cities_scores[city]
            current_armies -= j
        temporary_imperium.append([city, j+1]) # add the army that i previously removed
    return temporary_imperium

def produce(player, metropoles, cities, routes, imp1, h1, imp2, h2):

    # rename players
    enemy_player = 1 if (player == 2) else 2
    imp = imp1 if (player == 1) else imp2
    enemy_imp = imp2 if (player == 1) else imp1
    harvest = h1 if (player == 1) else h2
    enemy_harvest = h2 if (player == 1) else h1

    # get previous ammount of armies
    current_armies = 0
    for city in imp.values():
        current_armies += city.get_armies()

    # remove 1 army for every city so that im not left with cities with 0 armies
    for city in imp.keys(): # every city must have at least 1 army
        current_armies -= 1

    convertible_armies = current_armies
    if current_armies > 5:
         convertible_armies = 5

    temporary_harvest = harvest
    temporary_imperium = []

    # if I can with the game by having > 100 armies, I do so
    if harvest + convertible_armies >= 100:
        current_armies -= convertible_armies
        temporary_harvest += convertible_armies

        temporary_imperium = safeguard_metropolis(player, metropoles, cities, routes, imp, enemy_imp, current_armies) #I dont care about what happens to the rest of the cities
    else:
        if harvest >= 20:
            current_armies -= convertible_armies
            temporary_harvest += convertible_armies
        current_armies += harvest * 2
        temporary_harvest-= harvest

        temporary_imperium = maximize_armies_on_important_cities(player, metropoles, cities, routes, imp, enemy_imp, enemy_player,  current_armies)

    return temporary_harvest, temporary_imperium
