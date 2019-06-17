#
# - ciudades: lista - elemento = (ciudad, cant_especia)
# - rutas: diccionario - (K, V) = ((c1, c2), capacidad)
# - s1: seleccion del jugador 1 = lista de ciudades
# - s2: seleccion del jugador 2 = lista de ciudades
#
# return:
#   - imperio de cada una de las metropoli (imperio_1, imperio_2)
#       imperio_i: lista - elemento = (ciudad, cant_ejercito)
#           cant_ejercito es igual a 1 inicialmente
#
def divide(ciudades, rutas, s1, s2):

    metro1 = ciudades[0][0]
    metro2 = ciudades[1][0]

    dominadas = {}

    tope = min(len(s1), len(s2))

    for i in range(tope):
        c1 = s1[i]
        c2 = s2[i]
        if c1 != c2:
            if c1 not in dominadas:
                dominadas[c1] = 1
            if c2 not in dominadas:
                dominadas[c2] = 2
    i += 1

    if i == len(s1):
        for j in range(i, len(s2)):
            c = s2[j]
            if c not in dominadas:
                dominadas[c] = 2

    if i == len(s2):
        for j in range(i, len(s1)):
            c = s1[j]
            if c not in dominadas:
                dominadas[c] = 1

    imp1 = [(metro1, 1)]
    imp2 = [(metro2, 1)]

    for e in dominadas.items():
        if e[1] == 1:
            imp1.append((e[0], 1))
        else:
            imp2.append((e[0], 1))

    return imp1, imp2

def test(msg, ciudades, s1, s2):

    print(msg)

    i1, i2 = divide(ciudades, {}, s1, s2)

    print(i1)
    print(i2)
    print("")

if __name__ == "__main__":

    ciudades = [("Buenos Aires", 0), ("Moscu", 0)]

    test("Distintas e igual tamaño",
         ciudades,
         ["Montevideo", "Madrid", "Rio de Janeiro"],
         ["Roma", "Washigton", "Paris"])

    test("Distintas y tamaño diferente",
         ciudades,
         ["Montevideo", "Madrid", "Rio de Janeiro"],
         ["Roma", "Washigton"])

    test("Iguales e igual tamaño",
         ciudades,
         ["Montevideo", "Madrid", "Rio de Janeiro"],
         ["Roma", "Madrid", "Barcelona"])

    test("Iguales y diferente tamaño",
         ciudades,
         ["Montevideo", "Madrid", "Rio de Janeiro"],
         ["Roma", "Madrid"])
