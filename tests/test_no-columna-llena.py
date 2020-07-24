from src.bingo import no_columna_llena
from src.bingo import carton_oficial
def test_no_columna_llena():
    mi_carton=carton_oficial()
    assert no_columna_llena(mi_carton) == True
