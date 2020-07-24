from src.bingo import carton_oficial
from src.bingo import uno_a_noventa

def test_uno_a_noventa():
    assert uno_a_noventa(carton_oficial()) == True
