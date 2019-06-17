#! /usr/bin/env python3

import sys
import csv
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from commands.divide import divide

IMPERIUM_FILE = "imperio{}.txt"

def write_file(i1, i2):

    with open(IMPERIUM_FILE.format(1), "w") as f:
        for city, army in i1:
            f.write(city + ',' + str(army) + '\n')

    with open(IMPERIUM_FILE.format(2), "w") as f:
        for city, army in i2:
            f.write(city + ',' + str(army) + '\n')

def main(cities_path, routes_path, s1_path, s2_path):

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

    s1 = []

    with open(s1_path) as f:
        lines = f.readlines()
        for l in lines:
            s1.append(l.strip("\n"))

    s2 = []

    with open(s2_path) as f:
        lines = f.readlines()
        for l in lines:
            s2.append(l.strip("\n"))

    i1, i2 = divide(cities, routes, s1, s2)

    write_file(i1, i2)

def parse_input(params):

    if len(params) != 5:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: division.py [ciudades.txt] [rutas.txt] [seleccion1.txt] [seleccion2.txt]")
        return None

    cities = params[1]
    routes = params[2]
    s1 = params[3]
    s2 = params[4]

    return {
            "cities": cities,
            "routes": routes,
            "s-player-1": s1,
            "s-player-2": s2
    }

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["cities"],
             params["routes"],
             params["s-player-1"],
             params["s-player-2"])

