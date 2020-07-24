from src.bingo import no_tres_vacias
from src.bingo import carton_oficial
def test_no_tres_vacias():
    mi_carton=carton_oficial()
    assert no_tres_vacias(mi_carton) == True
