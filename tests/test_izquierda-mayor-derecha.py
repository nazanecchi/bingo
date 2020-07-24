from src.bingo import izq_may_der
from src.bingo import carton_oficial
def test_izq_may_der():
    mi_carton=carton_oficial()
    assert izq_may_der(mi_carton) == True
