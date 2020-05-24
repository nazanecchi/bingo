from src.bingo import carton

def test_cinco_por_fila():
    mi_carton=carton()
    for fila in range(0,3):
        con=0
        for columna in range (0,9):
            if(mi_carton[fila][columna]>0):
                con=con+1
        assert con==5
