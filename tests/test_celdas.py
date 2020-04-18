from src.bingo import carton

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
