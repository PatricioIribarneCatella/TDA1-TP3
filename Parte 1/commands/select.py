#
# - jugador: valor entero - {1,2}
# - ciudades: lista - elemento = (ciudad, cant_especia)
# - rutas: diccionario - (K, V) = ((c1, c2), capacidad)
#
# return:
#   - lista de ciudades ordenadas por prioridad
#
def select(jugador, ciudades, rutas):

    selec = []
    metropoli = ciudades[jugador - 1][0]

    # Las dos primeras ciudades son
    # las metropoli de cada uno de
    # los jugadores
    posibles_ciudades = ciudades[2:]

    # Se ordenan las ciudades por cantidad
    # de especia que pueden producir
    posibles_ciudades = sorted(posibles_ciudades,
                                key=lambda x: x[1],
                                reverse=True)

    for ciudad, cant in posibles_ciudades:
        if (ciudad, metropoli) in rutas:
            selec.append(ciudad)

    return selec

if __name__ == "__main__":

    ciudades = [("Buenos Aires", 0),
            ("Moscu", 0),
            ("Rio de Janeiro", 3),
            ("Washigton", 2),
            ("Roma", 6),
            ("Madrid", 4),
            ("Montevideo", 5)]
   
    rutas = {("Buenos Aires", "Montevideo"): 3,
            ("Buenos Aires", "Madrid"): 4,
            ("Buenos Aires", "Rio de Janeiro"): 7,
            ("Moscu", "Roma"): 6,
            ("Moscu", "Washigton"): 3}

    print(select(1, ciudades, rutas))
    print(select(2, ciudades, rutas))
    
