from graph import Graph

def find(cities, c):
    for e in cities:
        if e[0] == c:
            return e[1]

def collect(player, cities, routes, imp, pharvest):
    
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
        g.add_edge(w, metropoli_num, routes[(mapping[w], metropoli)])

    # Add edges between cities
    for n, city1 in enumerate(imp.keys()):
        for k, city2 in enumerate(imp.keys()):
            if (city1, city2) in routes:
                g.add_edge(n + 1, k + 1, routes[city1, city2])

    # Get max flow
    flow = g.ford_fulkerson(0, metropoli_num)

    return flow + pharvest


