from commands.general_commands import flow

def collect(player, metropoles, cities, routes, imp, pharvest):
    return flow(player, metropoles, cities, routes, imp, None, None) + pharvest
