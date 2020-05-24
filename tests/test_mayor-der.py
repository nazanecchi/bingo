from src.bingo import carton

def may_a_der():
    mi_carton=carton()
    for fila in range(0,3):
        help=0
        for columna in range (0,9):
            if(carton[fila][columna]>0):
                celda=help
                help=carton[fila][columna]
                assert help>celda
