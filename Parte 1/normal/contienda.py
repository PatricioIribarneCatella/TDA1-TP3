#! /usr/bin/env python3

import sys
import csv
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from commands.contest import contest
from commands.general_commands import create_cities_dict
from commands.general_commands import create_imperium_dict
from commands.general_commands import create_attack_dict

IMPERIUM_FILE = "imperio{}.txt"

def write_file(player1, player2, imp1, imp2):

    with open(IMPERIUM_FILE.format(player1), "w") as f:
        for city, army in imp1:
            f.write("%s,army\n" % city,army)

    with open(IMPERIUM_FILE.format(player2), "w") as f:
        for city, army in imp2:
            f.write("%s,army\n" % city,army)

def main(cities_path, routes_path,
         imp1_path, imp2_path,
         attack1_path, attack2_path):

    cities = create_cities_dict(cities_path)
     imp1 = create_imperium_dict(imp1_path, 1)
     imp2 = create_imperium_dict(imp2_path, 2)
     attack1 = create_attack_dict(attack1_path,1)
     attack2 = create_attack_dict(attack2_path,2)


    imp_1, imp_2 = contest(cities, imp1, imp2, attack1, attack2)

    write_file(1, 2, imp_1, imp_2)

def parse_input(params):

    if len(params) != 7:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: contienda.py [ciudades.txt] [rutas.txt] [imperio1.txt] [imperio2.txt] [ataque2.txt] [ataque2.txt]")
        return None

    cities = params[1]
    routes = params[2]
    imp1 = params[3]
    imp2 = params[4]
    attack1 = params[5]
    attack1 = params[6]

    return {
            "cities": cities,
            "routes": routes,
            "imp-1": imp1,
            "imp-2": imp2,
            "attack-1": attack1,
            "attack-2": attack2
    }

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["cities"],
             params["routes"],
             params["imp-1"],
             params["imp-1"],
             params["attack-2"],
             params["attack-2"])
