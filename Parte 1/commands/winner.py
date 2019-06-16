def fifty_rounds_winner(round, harvest1, harvest2, imperium1, imperium2, routes):
    winner = None
    if round < 50:
        return winner
    else:
        if harvest1>harvest2:
            winner = 1
        elif harvest2>harvest1:
            winner = 2
        else:
            if len(imperium1)>len(imperium2):
                winner = 1
            elif len(imperium2)>len(imperium2):
                winner = 2
            else:
                if sum(imperium1.values())>sum(imperium2.values()):
                    winner = 1
                elif sum(imperium2.values())>sum(imperium1.values()):
                    winner = 2
    return winner


def metropolis_is_disconnected(metropoles, routes, imperium, player):
    player_metropolis = None
    for name, metropolis in metropoles.items():
        if metropolis.superpower() == player:
            player_metropolis = name

    for origin, destinations in routes.items():
        if imperium.has_key(origin) and destinations.has_key(player_metropolis):
                return False
    return True

def disconection_winner(metropoles, routes, imperium1, imperium2):
    winner = None
    if metropolis_is_disconnected(metropoles, routes, imperium1, 1):
        winner = 2
    elif metropolis_is_disconnected(metropoles, routes, imperium2, 2):
        winner = 1
    return winner

def harvest_winner(harvest1, harvest2):
    winner = None
    if harvest1 >= 100 or harvest2>= 100:
        if harvest1>harvest2:
            winner = 1
        else:
            winner = 2
