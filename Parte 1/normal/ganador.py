#! /usr/bin/env python3

import sys
import csv
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from commands.general_command import create_metropolis_dict
from commands.general_command import create_cities_dict
from commands.general_command import create_routes_dict
from commands.general_command import create_imperium_dict

WINNER_FILE = "ganador.txt"


def create_winner_file(self, winner):
        with open(WINNER_FILE, "w") as winner_file:
                winner_file.write("%s\n" % winner)

def main(self, round, cities, routes, imperium1, harvest1, imperium2, harvest2):

    winner = None

    metropoles = create_metropolis_dict(cities)

    cities = create_cities_dict(cities)
    routes = create_routes_dict(routes)

    imperium1 = create_imperium_dict(imperium1, 1)
    imperium2 = create_imperium_dict(imperium2, 2)

    harvest1 = get_harvest(harvest1)
    harvest2 = get_harvest(harvest2)

    harvest_winner = harvest_winner(harvest1, harvest2)
    if harvest_winner:
        winner = harvest_winner
    else:
        disconection_winner = disconection_winner(cities, routes, imperium1, imperium2)
        if disconection_winner:
            winner = disconection_winner
        else:
            winner = fifty_rounds_winner(harvest1, harvest2, imperium1, imperium2)

    create_winner_file(self, winner)

def parse_input(params):

    if len(params) != 8:
        print("Error: cantidad insuficiente de parámetros")
        print("Formato: ganador.py [ronda] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]")
        return None

    round = int(params[1])

    cities = params[2]
    routes = params[3]
    imperium1 = params[4]
    harvest1 = params[5]
    imperium2 = params[6]
    harvest2 = params[7]

    return {
            "round": round,
            "cities": cities,
            "routes": routes,
            "imperium1":imperium1,
            "harvest1":harvest1,
            "imperium2":imperium2,
            "harvest2":harvest2
    }

if __name__ == "__main__":

    params = parse_input(sys.argv)

    if params is not None:
        main(params["round"],
             params["cities"],
             params["routes"],
             params["imperium1"],
             params["harvest1"],
             params["imperium2"],
             params["harvest2"])
