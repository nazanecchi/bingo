from src.bingo import carton

def test_no_tres_vacias():
    mi_carton=carton()
    con=0
    for fila in range(0,3):
        con=0
        for columna in range(0,9):
            if(mi_carton[fila][columna]==0):
                con=con+1
            if(mi_carton[fila][columna]!=0):
                con=0
            assert con<3
