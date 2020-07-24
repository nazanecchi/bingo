from src.bingo import mostrar_fila
from src.bingo import mostrar_columna
from src.bingo import contar_celdas_ocupadas_mayores
from src.bingo import contar_celdas_ocupadas_menores
from src.bingo import columnas_con_contenido
from src.bingo import filas_con_contenido
from src.bingo import carton_oficial
def test_celdas():
    mi_carton=carton_oficial()
    assert contar_celdas_ocupadas_mayores(mi_carton) == True and contar_celdas_ocupadas_menores(mi_carton) == True and columnas_con_contenido(mi_carton) == True and filas_con_contenido(mi_carton) == True
