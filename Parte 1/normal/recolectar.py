#! /usr/bin/env python3

import sys
import csv
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from commands.collect import collect

HARVEST_FILE = "cosecha{}.txt"

def write_file(harvest, player):

    with open(HARVEST_FILE.format(player), "w") as f:
        f.write(str(harvest) + '\n')

def main(player, cities_path, routes_path, imp_path):

    metropoles = create_metropolis_dict(cities_path)
    cities = create_cities_dict(cities_path)
    routes = create_routes_dict(routes_path)
    imp = create_imperium_dict(imp_path, player)
    pharvest = get_harvest(HARVEST_FILE.format(player))

    harvest = collect(player, metropoles, cities, routes, imp, pharvest)

    write_file(harvest, player)

def parse_input(params):

    if len(params) != 5:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: recolectar.py [jugador] [ciudades.txt] [rutas.txt] [imperio[i].txt]")
        return None

    player = int(params[1])
    cities = params[2]
    routes = params[3]
    imp = params[4]

    return {
            "player": player,
            "cities": cities,
            "routes": routes,
            "imp": imp
    }

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["player"],
             params["cities"],
             params["routes"],
             params["imp"])
