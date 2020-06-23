from src.bingo import carton
from src.bingo import mostrar_fila
from src.bingo import mostrar_columna
from src.bingo import test_contar_celdas_ocupadas_mayores
from src.bingo import test_contar_celdas_ocupadas_menores
from src.bingo import test_columnas_con_contenido
from src.bingo import test_filas_con_contenido

assert test_contar_celdas_ocupadas_mayores() == True and test_contar_celdas_ocupadas_menores() == True and test_columnas_con_contenido() == True and test_filas_con_contenido() == True
