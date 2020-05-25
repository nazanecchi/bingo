from src.bingo import carton

def test_no_columna_llena():
    mi_carton=carton()
    for columna in range(0,9):
        con=0
        for fila in range (0,3):
            if(mi_carton[fila][columna]>0):
                con=con+1
        assert con<3
