#! /usr/bin/env python3

import sys
import csv
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from commands.tactic import tactic
from commands.general_commands import create_cities_dict
from commands.general_commands import create_routes_dict
from commands.general_commands import create_imperium_dict
from commands.general_commands import create_metropolis_dict
from commands.general_commands import get_harvest

ATTACK_FILE = "ataque{}.txt"

def write_file(player, attack):

    with open(ATTACK_FILE.format(player), "w") as f:
        for c1, c2, army in attack:
            f.write(c1 + "," + c2 + "," + str(army) + '\n')

def main(player, cities_path, routes_path,
         imp1_path, harvest1_path,
         imp2_path, harvest2_path):

    metropoles = create_metropolis_dict(cities_path)
    cities = create_cities_dict(cities_path)
    routes = create_routes_dict(routes_path)
    imp1 = create_imperium_dict(imp1_path, 1)
    imp2 = create_imperium_dict(imp2_path, 2)
    h1 = get_harvest(harvest1_path)
    h2 = get_harvest(harvest2_path)


    attack = tactic(player, metropoles, cities, routes, imp1, h1, imp2, h2)

    write_file(player, attack)

def parse_input(params):

    if len(params) != 8:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: tactica.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]")
        return None

    player = int(params[1])
    cities = params[2]
    routes = params[3]
    imp1 = params[4]
    harvest1 = params[5]
    imp2 = params[6]
    harvest2 = params[7]

    return {
            "player": player,
            "cities": cities,
            "routes": routes,
            "imp-1": imp1,
            "harvest-1": harvest1,
            "imp-2": imp2,
            "harvest-2": harvest2
    }

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["player"],
             params["cities"],
             params["routes"],
             params["imp-1"],
             params["harvest-1"],
             params["imp-2"],
             params["harvest-2"])
