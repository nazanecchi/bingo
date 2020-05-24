from src.bingo import carton

def test_may_arriba_abajo():
    mi_carton=carton()
    for columna in range(0,9):
        help=0
        for fila in range (0,3):
            if(mi_carton[fila][columna]>0):
                celda=help
                help=mi_carton[fila][columna]
                assert help>celda
