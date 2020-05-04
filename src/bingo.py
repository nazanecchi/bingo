def carton():
    carton = (
    (1,0,1,0,1,0,0,0,1),
    (1,1,0,1,0,1,0,1,1),
    (1,0,0,1,1,0,1,0,1),
)
    return carton

def mostrar_fila(carton, nro_fila):
    return( carton[nro_fila][0],
            carton[nro_fila][1],
            carton[nro_fila][2],
            carton[nro_fila][3],
            carton[nro_fila][4],
            carton[nro_fila][5],
            carton[nro_fila][6],
            carton[nro_fila][7],
            carton[nro_fila][8],
            )

print (mostrar_fila(carton(), 1))
