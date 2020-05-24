from src.bingo import carton
from src.bingo import mostrar_fila
from src.bingo import mostrar_columna

def test_contar_celdas_ocupadas_mayores():
    carton1 = carton()
    contador = 0
    for fila in carton1:
        for celda in fila:
            contador += celda
    assert contador <= 15

def test_contar_celdas_ocupadas_menores():
    carton1 = carton()
    contador = 0
    for fila in carton1:
        for celda in fila:
            contador += celda
    assert contador  >=15

def test_columnas_con_contenido():
    a=0
    for con in range(9):
        aux=mostrar_columna(carton(), con)
        if(aux[0]+aux[1]+aux[2] == 0):
            a=1
    assert a==0


def test_filas_con_contenido():
    a=0
    for con in range(3):
        aux=mostrar_fila(carton(), con)
        if(aux[0]+aux[1]+aux[2]+aux[3]+aux[4]+aux[5]+aux[6]+aux[7]+aux[8] == 0):
            a=1
    assert a==0
