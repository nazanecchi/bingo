from src.bingo import carton

def test_no_numeros_repetidos():
    mi_carton=carton()
    for con in range(0,27):
        for fila in range(0,3):
            for columna in range (0,9):
                if(mi_carton[fila][columna]>0):
                    help=mi_carton[fila][columna]
                    for fila1 in range(0,3):
                        for columna1 in range (0,9):
                            if(mi_carton[fila1][columna1]>0 and (fila1!=fila or columna1!=columna)):
                                assert help!=mi_carton[fila1][columna1]
