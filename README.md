# TDA1-TP3

_La especia debe fluir_

### Run

Se puede ejecutar tanto la estrategia _normal_ o _dummy_ que se encuentran en el directorio con su respectivo nombre.

_estrategia_ = [normal | dummy]

- Selección

```bash
 $ python3 estrategia/seleccion.py [jugador] [ciudades.txt] [rutas.txt]

   genera: seleccion[jugador].txt 
```

- División

```bash
 $ python3 estrategia/division.py [ciudades.txt] [rutas.txt] [seleccion1.txt] [seleccion2.txt]

   genera: imperio1.txt e imperio2.txt 
```

- Recolectar

```bash
 $ python3 estrategia/recolectar.py [jugador] [ciudades.txt] [rutas.txt] [imperio[i].txt]

   genera: cosecha[jugador].txt 
```

- Producir

```bash
 $ python3 estrategia/producir.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]

   genera: cosecha[jugador]_temp.txt y imperio[jugador]_temp.txt
```
- Táctica

```bash
 $ python3 estrategia/tactica.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]

   genera: ataque[jugador].txt 
```

- Contienda

```bash
 $ python3 estrategia/contienda.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [imperio2.txt] [ataque1.txt] [ataque2.txt]

   actualiza: imperio1.txt e imperio2.txt 
```

- Ganador

```bash
 $ python3 estrategia/ganador.py [ronda] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]

   genera: ganador.txt
```

### Clean

```bash
 $ ./clean.sh
```
