from commands.city import City
from commands.metropolis import Metropolis

def join_armies(attack):
    joint_attack = {}
    for origin, destinations in attack.items():
        for destination, army in destinations.items():
            if destination not in joint_attack:
                joint_attack[destination] = 0
            joint_attack[destination] += army
    return joint_attack

def remove_attacking_armies(imperium, attack):
    defense_imperium = {}
    for city in imperium.keys():
        if city in attack:
            defense_imperium[city] = imperium[city].get_armies() - sum(attack[city].values())
        else:
            defense_imperium[city] = imperium[city].get_armies()
    return defense_imperium

def contest(cities, imp1, imp2, attack1, attack2):

    defense_imperium1 = remove_attacking_armies(imp1, attack1)
    defense_imperium2 = remove_attacking_armies(imp2, attack2)

    print("defense_imperium1: ", defense_imperium1)
    print("defense_imperium2: ", defense_imperium2)

    print("attack1: ", attack1)
    print("attack2: ", attack2)

    joint_armies1 = join_armies(attack1)
    joint_armies2 = join_armies(attack2)

    print("joint_armies1: ", joint_armies1)
    print("joint_armies2: ", joint_armies2)

    imp_1 = {}
    imp_2 = {}
    for city in cities.keys():
        if city in defense_imperium1 and not city in joint_armies2:
            imp_1[city] = defense_imperium1[city]
        elif city in defense_imperium2 and not city in joint_armies1:
            imp_2[city] = defense_imperium2[city]
        elif city in joint_armies1 and city in joint_armies2:
            if joint_armies1[city]>joint_armies2[city]:
                imp_1[city] = joint_armies1[city]-joint_armies2[city]
            else:
                imp_2[city] = joint_armies2[city]-joint_armies1[city]
        elif city in defense_imperium1 and city in joint_armies2:
            if defense_imperium1[city] > joint_armies2[city]:
                imp_1[city] = defense_imperium1[city] - joint_armies2[city]
            elif defense_imperium1[city] < joint_armies2[city]:
                imp_2[city] = joint_armies2[city]- defense_imperium1[city]
        elif city in defense_imperium2 and city in joint_armies1:
            if defense_imperium2[city] > joint_armies1[city]:
                imp_2[city] = defense_imperium2[city] - joint_armies1[city]
            elif defense_imperium2[city] < joint_armies1[city]:
                imp_1[city] = joint_armies1[city]- defense_imperium2[city]
    return imp_1, imp_2
