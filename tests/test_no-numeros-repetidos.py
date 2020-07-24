from src.bingo import no_numeros_repetidos
from src.bingo import carton_oficial
def test_no_numeros_repetidos():
    mi_carton=carton_oficial()
    assert no_numeros_repetidos(mi_carton) == True
