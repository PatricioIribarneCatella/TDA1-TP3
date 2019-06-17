import math
from graph import Graph

def find(cities, c):
    for e in cities:
        if e[0] == c:
            return e[1]

def flow(player, cities, routes, imp, added_city, removed_city):
    if added_city:
        imp[added_city] = City(added_city)
    if removed_city:
        if imp.has_key(removed_city):
            imp.pop(removed_city)

    metropoli = cities[player - 1][0]

    g = Graph(True)

    g.add_node(0, "source")

    mapping = {}
    for e in enumerate(imp.keys()):
        g.add_node(e[0] + 1, e[1])
        mapping[e[0] + 1] = e[1]

    g.add_node(e[0] + 2, metropoli)
    metropoli_num = e[0] + 2

    # Add edges between "source" and
    # cities. Flow capacity in the edge is the
    # max production capacity of the city
    for v in range(1, len(imp.keys()) + 1):
        g.add_edge(0, v, find(cities, mapping[v]))

    # Add edges between cities and "metropoli"
    for w in range(1, len(imp.keys()) + 1):
        if (mapping[w], metropoli) in routes:
            g.add_edge(w, metropoli_num, routes[(mapping[w], metropoli)])

    # Add edges between cities
    for n, city1 in enumerate(imp.keys()):
        for k, city2 in enumerate(imp.keys()):
            if (city1, city2) in routes:
                g.add_edge(n + 1, k + 1, routes[city1, city2])

    # Get max flow
    flow = g.ford_fulkerson(0, metropoli_num)

    return flow

def are_neighbours(city, other_city, routes):
    return routes[city].has_key(other_city) or routes[other_city].has_key(city)

def safeguard_metropolis(player, metropoles, cities, routes, imp, enemy_imp, current_armies):
    metripolis = get_metropolis(metropoles, player)
    metropolis_neighbours= {}
    for city in imp.keys():
        if are_neighbours(city, metripolis, routes):
            metropolis_neighbours[city] = 0

    for city in metropolis_neighbours.keys():
        for enemy_city in enemy_imp.keys():
            if are_neighbours(city, enemy_city, routes):
                metropolis_neighbours[destination] += 1

    selected_neighbour = None
    for neighbour in metropolis_neighbours.keys():
        if not selected_neighbour:
            selected_neighbour = neighbour
        if metropolis_neighbours[neighbour] < metropolis_neighbours[selected_neighbour]:
            selected_neighbour = neighbour

    temporary_imperium = []
    for city in imp,keys():
        armies = 1
        if city == selected_neighbour:
            armies += current_armies
        temporary_imperium.append([city, armies])

    return temporary_imperium



def maximize_armies_on_important_cities(player, cities, cities_dict, routes, imp, harvest, enemy_imp, enemy_harvest):
    #calculate score for every enemy city
    enemy_cities_scores = {}
    for enemy_city in cities_dict.keys(): #I have to consider cities that are not in the enemy imperium nor in mine
        if not cities_dict[enemy_city].is_metropolis() and not imp.has_key(enemy_city):
            a = flow(player, cities, routes, imp, None, None) # calculate flow from imp1 city to my metropolis
            b = flow(player, cities, routes, imp, enemy_city, None) # calculate flow from imp1 plus enemy city to my metropolis
            c = b-a
            e = flow(enemy_player, cities, routes, enemy_imp, None, None) # calculate flow from imp2 city to enemy metropolis
            f = flow(enemy_player, cities, routes, enemy_imp, None, enemy_city) # calculate flow from imp2 minus enemy city to enemy metropolis
            g = e-f
            h = cities_dict[enemy_city].production() # enemy_city species production

            i = c + g + d # how valuable is enemy_city
            enemy_cities_scores[enemy_city] = i

    # add sum of neighbour enemy city scores to every city
    cities_scores = {}
    for city in imp.keys():
        # total score of neighbouring enemy cities
        j = 0
        for enemy_city in cities_dict.keys():
            if enemy_cities_scores.has_key(enemy_city) and are_neighbours(city, enemy_city, routes):
                j += enemy_cities_scores[enemy_city]
        cities_scores[city] = j

    temporary_imperium = []

    sorted_cities = cities_scores.keys()
    sorted_cities.sort(key=lambda x: cities_scores[x], reverse=True)
    x = sum(cities_scores.values())

    for city in sorted_cities:
        j= 0
        if current_armies > 0:
            j = math.ceil(current_armies * (cities_scores[city]/float(x)))
            x -= cities_scores[city]
            current_armies -= j
        temporary_imperium.append([city, j+1]) # add the army that i previously removed
    return

def produce(player, metropoles, cities, cities_dict, routes, imp1, h1, imp2, h2):

    # rename players
    enemy_player = 1 if player == 2 else 2
    imp = imp1 if player == 1 else imp2
    enemy_imp = imp2 if player == 1 else imp1
    harvest = h1 if player == 1 else h2
    enemy_harvest = h2 if player == 1 else h1

    # get previous ammount of armies
    current_armies = 0
    for city in imp.values():
        current_armies += city.armies()

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

        temporary_imperium = maximize_armies_on_important_cities(player, cities, cities_dict, routes, imp, harvest, enemy_imp, enemy_harvest):

    return temporary_harvest, temporary_imperium
