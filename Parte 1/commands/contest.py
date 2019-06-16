def join_armies(attack):
    attack = {}
    for origin, destinations in attack.items():
        for destination, army in destinations.items():
            if not attack.has_key(destination):
                attack[destination] = 0
            attack[destination] += army

def remove_attacking_armies(imperium, attack):
    defense_imperium = {}
    for city in imperium.keys():
        if attack.has_key(city):
            defense_imperium[city] = imperium[city].armies() - sum(attack[city].values())
    return defense_imperium

def contest(cities, imp1, imp2, attack1, attack2):

    defense_imperium1 = remove_attacking_armies(imp1, attack1)
    defense_imperium2 = remove_attacking_armies(imp2, attack2)

    joint_armies1 = join_armies(attack1)
    joint_armies2 = join_armies(attack2)

    imp_1 = {}
    imp_2 = {}
    for city_name, city in cities:
        if city_name in defense_imperium1 and not city_name in joint_armies2:
            imp_1[city_name] = defense_imperium1[city_name]
        elif city_name in defense_imperium2 and not city_name in joint_armies1:
            imp_2[city_name] = defense_imperium2[city_name]
        elif city_name in joint_armies1 and city_name in joint_armies2:
            if joint_armies1[city_name]>joint_armies2[city_name]:
                imp_1[city_name] = joint_armies1[city_name]-joint_armies2[city_name]
            else:
                imp_2[city_name] = joint_armies2[city_name]-joint_armies1[city_name]
        elif city_name in defense_imperium1 and city_name in joint_armies2:
            if defense_imperium1[city_name] > joint_armies2[city_name]:
                imp_1[city_name] = defense_imperium1[city_name] - joint_armies2[city_name]
            elif defense_imperium1[city_name] < joint_armies2[city_name]:
                imp_2[city_name] = joint_armies2[city_name]- defense_imperium1[city_name]
        elif city_name in defense_imperium2 and city_name in joint_armies1:
            if defense_imperium2[city_name] > joint_armies1[city_name]:
                imp_2[city_name] = defense_imperium2[city_name] - joint_armies1[city_name]
            elif defense_imperium2[city_name] < joint_armies1[city_name]:
                imp_1[city_name] = joint_armies1[city_name]- defense_imperium2[city_name]
    return imp_1, imp_2
