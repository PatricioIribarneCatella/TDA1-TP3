def create_metropolis_dict(self, cities_file_name):
    with open(cities_file_name) as cities_file:
    cities_csv = csv.reader(cities_file)
    metropolis = {}
    name, production = cities_csv.readline()
    metropolis[name] = Metropolis(name, 1)
    name, production = cities_csv.readline()
    metropolis[name] = Metropolis(name, 2)
    return metropolis

def create_cities_dict(self, cities_file_name):
    with open(cities_file_name) as cities_file:
    cities_csv = csv.reader(cities_file)
    cities = {}
    counter = 1
    for name, production in cities_csv:
        if counter <= 2:
            city = Metropolis(name, counter)
        else:
            city = City(name)
        city.set_production(production)
        cities[name] = city
        counter += 1
    return cities

def create_routes_dict(self, routes_file_name):
    with open(routes_file_name) as routes_file:
    routes_csv = csv.reader(routes_file)
    routes = {}
    for origin, destination, production in routes_csv:
        routes[origin][destination] = production
    return metropolis, cities

def create_imperium_dict(self, imperium_file_name, player):
    with open(imperium_file_name) as imperium_file:
    imperium_csv = csv.reader(imperium_file)
    imperium = {}
    counter = 1
    for name, armies in imperium_csv:
        if couter == 1:
            city = Metropolis(name, player)
        else:
            city = City(name)
        city.set_armies(armies)
        imperium[name] = city
        counter += 1
    return imperium
