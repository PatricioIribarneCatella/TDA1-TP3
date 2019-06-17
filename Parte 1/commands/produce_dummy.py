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
            metropolis_neighbours.add(city)

    selected_neighbour = metropolis_neighbours.pop()

    temporary_imperium = []
    for city in imp.keys():
        armies = 1
        if city == selected_neighbour:
            armies += current_armies
        temporary_imperium.append([city, armies])

    return temporary_imperium

def maximize_armies_on_important_cities(player, metropoles, cities, routes, imp, harvest, enemy_imp, enemy_harvest, enemy_player,  current_armies):
    temporary_imperium_dic = {}
    for city in imp.keys():
        temporary_imperium_dic[city] = 1

    while current_armies > 0:
        for city in imp.keys():
            if current_armies > 0:
                temporary_imperium_dic[city] += 1
                current_armies-= 1

    temporary_imperium = []
    for city, armies in temporary_imperium_dic.items():
        temporary_imperium.append([city, armies])

    return temporary_imperium

def produce_dummy(player, metropoles, cities, routes, imp1, h1, imp2, h2):

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

        temporary_imperium = maximize_armies_on_important_cities(player, metropoles, cities, routes, imp, harvest, enemy_imp, enemy_harvest, enemy_player,  current_armies)

    return temporary_harvest, temporary_imperium
