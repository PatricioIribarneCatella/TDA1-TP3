from graph import Graph
#
# - player: inv value - {1,2}
# - cities: list - element = (city, species)
# - routes: dictionary of dictionaries - (K, V) = ((c1, c2), capacidad)
#
# return:
#   - list of cities ordered by priority
#
def select(player, cities, routes):

    selection = []
    metropolis, production = cities[player - 1]

    levels, max_level = determine_levels(metropolis, cities, routes)

    extended_cities = []
    # The first two cities are metropolis
    for name, production in cities[2:]:
        city = (name, production, max_level - levels[name])
        extended_cities.append(city)


    # We sort the cities first by their distance to the
    # metripolis and then by their species production
    extended_cities = sorted(extended_cities,
                                key=lambda x: (x[2], x[1]),
                                reverse=True)

    for name, production, level in extended_cities:
        selection.append(name)

    return selection

def determine_levels(metropolis, cities, routes):

    g = Graph(True)

    for name, production in cities:
        g.add_node(name)

    for origin, destinations in routes.items():
            for destination in destinations.keys():
                    g.add_edge(origin, destination, routes[origin][destination])

    # Get levels
    levels = g.levels(metropolis)
    return levels

if __name__ == "__main__":

    cities = [("Buenos Aires", 0),
            ("Moscu", 0),
            ("Rio de Janeiro", 3),
            ("Washigton", 2),
            ("Roma", 6),
            ("Madrid", 4),
            ("Montevideo", 5)]

    routes = {
            "Buenos Aires": {
                "Montevideo": 3,
                "Madrid": 4,
                "Rio de Janeiro": 7
            },
            "Moscu": {
                "Roma": 6,
                "Washigton": 3
            },
            "Madrid": {
                "Moscu": 3
            },
            "Roma": {
                "Buenos Aires": 3
            }
    }

    print(select(1, cities, routes))
    print(select(2, cities, routes))

