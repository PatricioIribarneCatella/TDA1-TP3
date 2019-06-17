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

def tactic(player, metropoles, cities, cities_dict, routes, imp1, h1, imp2, h2):

    # rename players
    enemy_player = 1 if player == 2 else 2
    imp = imp1 if player == 1 else imp2
    enemy_imp = imp2 if player == 1 else imp1
    harvest = h1 if player == 1 else h2
    enemy_harvest = h2 if player == 1 else h1

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

    attack = []
    for city in imp.keys():
        city_army = city.armies()
        attacking_force = city_army - 1

        # total score of neighbouring enemy cities
        x = 0
        for enemy_city in cities_dict.keys():
            if enemy_cities_scores.has_key(enemy_city) and are_neighbours(city, enemy_city, routes):
                x += enemy_cities_scores[enemy_city]

        for enemy_city in cities_dict.keys():
            if enemy_cities_scores.has_key(enemy_city) and are_neighbours(city, enemy_city, routes):
                j = math.ceil(attacking_force * (enemy_cities_scores[enemy_city]/float(x)))
                x -= enemy_cities_scores[enemy_city]
                if j > 0:
                    attack.append([city,enemy_city,j])
                attacking_force -= j
                if attacking_force <= 0:
                    break
    return attack
