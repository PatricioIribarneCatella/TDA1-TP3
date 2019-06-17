#! /usr/bin/env python3

import sys
import csv
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from commands.select_dummy import select_dummy
from commands.general_commands import create_routes_dict

SELECTION_FILE = "seleccion{}.txt"

def write_file(s, player):

    with open(SELECTION_FILE.format(player), "w") as f:
        for city in s:
            f.write(city + '\n')

def main(player, cities_path, routes_path):

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

    routes = create_routes_dict(routes_path)

    s = select_dummy(player, cities, routes)

    write_file(s, player)

def parse_input(params):

    if len(params) != 4:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: seleccion.py [jugador] [ciudades.txt] [rutas.txt]")
        return None

    player = int(params[1])

    cities = params[2]
    routes = params[3]

    return {
            "player": player,
            "cities": cities,
            "routes": routes
    }

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["player"],
             params["cities"],
             params["routes"])
