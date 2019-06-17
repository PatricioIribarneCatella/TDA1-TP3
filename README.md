# TDA1-TP3

_La especia debe fluir_

### Run

Se puede ejecutar tanto la estrategia _normal_ o _dummy_ que se encuentran en el directorio con su respectivo nombre.

_estrategia_ = [normal | dummy]

- Selección

```bash
 $ python3 _estrategia_/seleccion.py [jugador] [ciudades.txt] [rutas.txt]

   genera _seleccion[jugador].txt_
```

- División

```bash
 $ python3 _estrategia_/division.py [ciudades.txt] [rutas.txt] [seleccion1.txt] [seleccion2.txt]

   genera _imperio1.txt_ e _imperio2.txt_
```

- Recolectar

```bash
 $ python3 _estrategia_/recolectar.py [jugador] [ciudades.txt] [rutas.txt] [imperio[i].txt]

   genera _cosecha[jugador].txt_
```

- Producir

```bash
 $ python3 _estrategia_/producir.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]

   genera *cosecha[jugador]_temp.txt* y *imperio[jugador]_temp.txt*
```
- Táctica

```bash
 $ python3 _estrategia_/tactica.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]

   genera _ataque[jugador].txt_
```

- Contienda

```bash
 $ python3 _estrategia_/contienda.py [jugador] [ciudades.txt] [rutas.txt] [imperio1.txt] [imperio2.txt] [ataque1.txt] [ataque2.txt]

   actualiza _imperio1.txt_ _imperio2.txt_
```

- Ganador

```bash
 $ python3 _estrategia_/ganador.py [ronda] [ciudades.txt] [rutas.txt] [imperio1.txt] [cosecha1.txt] [imperio2.txt] [cosecha2.txt]

   actualiza _imperio1.txt_ _imperio2.txt_
```

### Clean

```bash
 $ ./clean.sh
```
