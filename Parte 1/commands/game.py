class Game():

    def __init__(self):

    def create_cities_dict(self, cities):
        with open(cities) as cities_file:
        cities_csv = csv.reader(cities_file)
        cities = {}
        counter = 1
        for name, production in cities_csv:
            if counter <= 2:
                cities[name] = Metropolis(name, production, player)
            else:
                cities[name] = City(name, production)
            counter += 1
        return cities

    def create_routes_dict(self, routes):
        with open(routes) as routes_file:
        routes_csv = csv.reader(routes_file)
        routes = {}
        for origin, destination, production in routes_csv:
            routes[origin][destination] = production
        return metropolis, cities

    def create_selection_file(self, cities_ordered_by_preference, player):
        f= open("seleccion%s.txt" % player,"w")
        for city in cities_ordered_by_preference:
            f.write("%s\n" % city)
        f.close()


    def selection(self, player, cities, routes):

        cities = create_cities_dict(player, cities)
        routes = create_routes_dict(routes)

        cities_ordered_by_preference = return [city_name for city_name, city in cities.values() if not city.is_metropolis()]

        cities_ordered_by_preference.sort(key = lambda city: calculate_preference_weight(city, metropolis[payer], cities, routes))

        create_selection_file(create_selection_file)

    def create_imperium_file(self, cities, player):
        f= open("imperio%s.txt" % player,"w")
        for city in cities.keys():
            f.write("%s,1\n" % city)
        f.close()

    def division(self, cities, routes, selection1, selection2):

        with open(selection1) as selection1_file:
        selection1_csv = csv.reader(selection1_file)
        selection1 = {}
        for city in selection1_csv:
            selection1[city] = True
        with open(selection2) as selection2_file:
        selection2_csv = csv.reader(selection2_file)
        selection2 = {}
        for city in selection2_csv:
            if selection1.has_key(city):
                selection1.pop(city)
            else:
                selection2[city] = True
        create_imperium_file(selection1, 1)
        create_imperium_file(selection1, 2)

    def get_current_harvest(self, player):
        with open("cosecha%s.txt" % player) as harvest_file:
        collect_csv = csv.reader(harvest_file)
        return harvest_csv.readline()

    def collect(self, player, imperium, cities, routes):

        current_harvest = get_current_harvest(player)
        new_harvest = calculate_harvest(player, imperium, cities, routes, current_harvest)

        f= open("cosecha%s.txt" % player,"w")
        f.write("%s\n" % new_harvest)
        f.close()

    def produce(self, player, cities, routes, imperium1, harvest1, imperium2, harvest2):

    def tactic(self, player, cities, routes, imperium1, harvest1, imperium2, harvest2):

    def contest(self, cities, routes, imperium1, imperium2, attacks1, attacks2):

    def winner(self, round, cities, routes, imperium1, harvest1, imperium2, harvest2):

    def calculate_preference_weight(self, city, metropolis, cities, routes):
        #TODO
    def calculate_harvest(self, player, imperium, cities, routes, current_harvest)
        #TODO
