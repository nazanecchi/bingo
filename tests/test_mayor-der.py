from src.bingo import may_a_der
from src.bingo import carton_oficial
def test_may_a_der():
    mi_carton=carton_oficial()
    assert may_a_der(mi_carton) == True
