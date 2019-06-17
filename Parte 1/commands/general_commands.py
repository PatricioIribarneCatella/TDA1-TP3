def create_metropolis_dict(cities_file_name):
    with open(cities_file_name) as cities_file:
    cities_csv = csv.reader(cities_file)
    metropolis = {}
    name, production = cities_csv.readline()
    metropolis[1] = [name, Metropolis(name, 1)]
    name, production = cities_csv.readline()
    metropolis[2] = [name, Metropolis(name, 2)]
    return metropolis

def create_cities_dict(cities_file_name):
    with open(cities_file_name) as cities_file:
    cities_csv = csv.reader(cities_file)
    cities = {}
    counter = 1
    for name, production in cities_csv:
        if counter <= 2:
            city = Metropolis(name, counter)
        else:
            city = City(name)
        city.set_production(int(production))
        cities[name] = city
        counter += 1
    return cities

def create_routes_dict(routes_file_name):
    with open(routes_file_name) as routes_file:
    routes_csv = csv.reader(routes_file)
    routes = {}
    for origin, destination, production in routes_csv:
        if not routes.has_key(origin):
            routes[origin] = {}
        routes[origin][destination] = int(capacity)
    return metropolis, cities

def create_imperium_dict(imperium_file_name, player):
    with open(imperium_file_name) as imperium_file:
    imperium_csv = csv.reader(imperium_file)
    imperium = {}
    counter = 1
    for name, armies in imperium_csv:
        if couter == 1:
            city = Metropolis(name, player)
        else:
            city = City(name)
        city.set_armies(int(armies))
        imperium[name] = city
        counter += 1
    return imperium

def create_attack_dict(attack1_path, player):
    with open(attack1_path) as attack_file:
    attack_csv = csv.reader(attack_file)
    attack = {}
    for origin, destination, armies in attack_csv:
        if not attack.has_key(origin):
            attack[origin] = {}
        attack[origin][destination] = int(armies)
    return attack

def get_harvest(harvest_file_name):
    with open(harvest_file_name) as harvest_file:
    collect_csv = csv.reader(harvest_file)
    return int(harvest_csv.readline()[0])

def get_metropolis(metropoles, player):
    name, metropolis = metropoles[player]
    return name

def are_neighbours(city, other_city, routes):
    return routes[city].has_key(other_city) or routes[other_city].has_key(city)

def flow(player, metropoles, cities, routes, imp, added_city = None, removed_city = None):
    if added_city:
        imp[added_city] = City(added_city)
    if removed_city:
        if imp.has_key(removed_city):
            imp.pop(removed_city)

    metropolis = get_metropolis(metropoles, player)
    g = Graph(True)

    start = "start"
    g.add_node(start)
    for city in imp.keys():
        g.add_node(city)

    for origin, destinations in routes.items():
        if origin in imp.keys():
            for destination in destinations.keys():
                if destination in imp.keys():
                    g.add_edge(origin, destination, routes[origin][destination])

    for city in imp.keys():
        g.add_edge(start, city, cities[origin].production())

    # Get max flow
    flow = g.ford_fulkerson(start, metropolis)
