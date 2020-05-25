from src.bingo import carton

def test_izq_may_der():
    mi_carton=carton()
    con=0
    for columna in range(0,8):
        for fila in range (0,3):
            if(mi_carton[fila][columna]>0):
                help=mi_carton[fila][columna]
                for fila1 in range (0,3):
                    if(mi_carton[fila1][columna+1]>0):
                        assert help<mi_carton[fila1][columna+1]
