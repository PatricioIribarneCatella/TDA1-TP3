#! /usr/bin/env python3

import sys
import csv
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from commands.collect import collect

HARVEST_FILE = "cosecha{}_temp.txt"
IMPERIUM_FILE = "imperio{}_temp.txt"

def write_file(player, harvest_temp, imp_temp):

    with open(HARVEST_FILE.format(player), "w") as f:
        f.write(str(harvest_temp) + '\n')

    with open(IMPERIUM_FILE.format(player), "w") as f:
        for city, army in imp_temp:
            f.write(city + ',' + str(army) + '\n')

def main(player, cities_path, routes_path,
         imp1_path, harvest1_path,
         imp2_path, harvest2_path):

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

    imp1 = {}

    with open(imp1_path) as f:
        imp_csv = csv.reader(f)
        for city, army in imp_csv:
            imp1[city] = int(army)

    imp2 = {}

    with open(imp2_path) as f:
        imp_csv = csv.reader(f)
        for city, army in imp_csv:
            imp2[city] = int(army)

    with open(harvest1_path) as f:
        h1 = f.readline()

    with open(harvest2_path) as f:
        h2 = f.readline()

    harvest_temp, imp_temp = produce(player, cities, routes, imp1, h1, imp2, h2)

    write_file(player, harvest_temp, imp_temp)

def parse_input(params):

    if len(params) != 8:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: producir.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]")
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
