from src.bingo import cinco_por_fila
from src.bingo import carton_oficial
def test_cinco_por_fila():
    mi_carton=carton_oficial()
    assert cinco_por_fila(mi_carton) == True
