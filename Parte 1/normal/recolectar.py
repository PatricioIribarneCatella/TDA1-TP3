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

    cities = []

    with open(cities_path) as f:
        cities_csv = csv.reader(f)
        counter = 1
        for name, production in cities_csv:
            if counter <= 2:
                cities.append((name, production))
            else:
                cities.append((name, production))
            counter += 1

    routes = {}

    with open(routes_path) as f:
        routes_csv = csv.reader(f)
        for origin, destination, capacity in routes_csv:
            routes[(origin, destination)] = capacity

    imp = {}

    with open(imp_path) as f:
        imp_csv = csv.reader(f)
        for city, army in imp_csv:
            imp[city] = int(army)

    try:
        with open(HARVEST_FILE.format(player)) as f:
            pharvest = f.readline()
    except FileNotFoundError:
        pharvest = 0

    harvest = collect(player, cities, routes, imp, pharvest)

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

