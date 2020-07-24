from src.bingo import may_arriba_abajo
from src.bingo import carton_oficial
def test_may_arriba_abajo():
    mi_carton=carton_oficial()
    assert may_arriba_abajo(mi_carton) == True
