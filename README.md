[![Build Status](https://travis-ci.com/nazaspu/bingo.svg?branch=master)](https://travis-ci.com/nazaspu/bingo)
[![Coverage Status](https://coveralls.io/repos/github/nazaspu/bingo/badge.svg?branch=master)](https://coveralls.io/github/nazaspu/bingo?branch=master)
# Bingo
Proyecto de Bingo que genera cartones validos a partir de ciertas condiciones Programa hecho por Rodrigo Marí, 6to año del Intituto Politecnico Superior
# REGLAS
Los cartones que se generen tendran las siguientes condiciones:

- Cada carton es una matrix de 3 x 9.
- Los números del carton se encuentran en el rango 1 a 90.
- Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90. 70 al 79 y 80 al 90.
- No hay números repetidos en el carton.
- Cada fila de un carton tiene exactamente 5 celdas ocupadas.
- Cada carton es una matrix de 3 x 9.
- Cada carton tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacias.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
- En una fila no existen más de dos celdas ocupadas consecutivas.
- En una fila no existen más de dos celdas vacías consecutivas.
Para generar un carton escribir en consola:

Bingo_dagos/src/bingo.py

Un ejemplo de carton válido podría ser el siguiente:

5 0 22 0 40 0 67 75 0

0 13 26 0 46 0 69 0 85

7 16 0 32 0 54 0 77 0
