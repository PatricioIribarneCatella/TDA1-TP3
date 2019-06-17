from general_commands import flow

def collect(player, metropoles, cities, routes, imp, pharvest):

    flow =  flow(player, metropoles, cities, routes, imp, None, None)

    return flow + pharvest
