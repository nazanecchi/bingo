import random
import math
def imprimirCarton(carton):
        for columna in range(3):
            for fila in range(9):
                if carton[columna][fila] > 9:
                    print(carton[columna][fila], end=' ')
                if carton[columna][fila] <= 9:
                    print(carton[columna][fila], end='  ')
            print('\n')



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

def mostrar_columna(carton, nro_columna):
        return( carton[0][nro_columna],
                carton[1][nro_columna],
                carton[2][nro_columna],
                )

def uno_a_noventa(mi_carton):
        contador=0
        con=0
        z=0
        for fila in range(0,3):
            for columna in range (0,9):
                celda=mi_carton[fila][columna]
                if(celda>=91 or celda<0):
                    z=1
        return (z==0)
def contar_celdas_ocupadas_mayores(mi_carton):
        carton1=mi_carton
        contador = 0
        for fila in carton1:
            for celda in fila:
                if(celda>0):
                    contador=contador+1
        return (contador <= 15)

def contar_celdas_ocupadas_menores(mi_carton):
        carton1 = mi_carton
        contador = 0
        for fila in carton1:
            for celda in fila:
                if(celda>0):
                    contador=contador+1
        return (contador  >=15)

def columnas_con_contenido(mi_carton):
        z=0
        for con in range(9):
            aux=mostrar_columna(mi_carton, con)
            if(aux[0]+aux[1]+aux[2] == 0):
                z=1
        return (z==0)


def filas_con_contenido(mi_carton):
        z=0
        for con in range(3):
            aux=mostrar_fila(mi_carton, con)
            if(aux[0]+aux[1]+aux[2]+aux[3]+aux[4]+aux[5]+aux[6]+aux[7]+aux[8] == 0):
                z=1
        return (z==0)

def no_tres_vacias(mi_carton):
        con=0
        z=0
        for fila in range(0,3):
            con=0
            for columna in range(0,9):
                if(mi_carton[fila][columna]==0):
                    con=con+1
                if(mi_carton[fila][columna]!=0):
                    con=0
                if (con>=3):
                    z=1
        return (z==0)
def no_tres_ocupadas(mi_carton):
        con=0
        z=0
        for fila in range(0,3):
            con=0
            for columna in range(0,9):
                if(mi_carton[fila][columna]!=0):
                    con=con+1
                if(mi_carton[fila][columna]==0):
                    con=0
                if (con>=3):
                    z=1
        return (z==0)
def no_numeros_repetidos(mi_carton):
        z=0
        for con in range(0,27):
            for fila in range(0,3):
                for columna in range (0,9):
                    if(mi_carton[fila][columna]>0):
                        help=mi_carton[fila][columna]
                        for fila1 in range(0,3):
                            for columna1 in range (0,9):
                                if(mi_carton[fila1][columna1]>0 and (fila1!=fila or columna1!=columna)):
                                    if (help==mi_carton[fila1][columna1]):
                                        z=1
        return (z==0)
def no_columna_llena(mi_carton):
        z=0
        for columna in range(0,9):
            con=0
            for fila in range (0,3):
                if(mi_carton[fila][columna]>0):
                    con=con+1
            if (con==3):
                z=1
        return (z==0)
def may_a_der(mi_carton):
        z=0
        for fila in range(0,3):
            help=0
            for columna in range (0,9):
                if(mi_carton[fila][columna]>0):
                    celda=help
                    help=mi_carton[fila][columna]
                    if(help<=celda):
                        z=1
        return z==0
def may_arriba_abajo(mi_carton):
        z=0
        for columna in range(0,9):
            help=0
            for fila in range (0,3):
                if(mi_carton[fila][columna]>0):
                    celda=help
                    help=mi_carton[fila][columna]
                    if (help<=celda):
                        z=1
        return(z==0)

def izq_may_der(mi_carton):
        con=0
        z=0
        for columna in range(0,8):
            for fila in range (0,3):
                if(mi_carton[fila][columna]>0):
                    help=mi_carton[fila][columna]
                    for fila1 in range (0,3):
                        if(mi_carton[fila1][columna+1]>0):
                            if(help>=mi_carton[fila1][columna+1]):
                                z=1
        return(z==0)

def cinco_por_fila(mi_carton):
        z=0
        for fila in range(0,3):
            con=0
            for columna in range (0,9):
                if(mi_carton[fila][columna]>0):
                    con=con+1
            if (con!=5):
                z=1
        return(z==0)
def carton_oficial():
    a=0
    while(a==0):
        def carton():

            contador = 0
            carton = (
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]
            )
            numerosCarton = 0

            while (numerosCarton < 15):
              contador = contador + 1
              if (contador == 50):
                return carton

              numero = random.randint(1,90)
              columna = int(math.floor(numero / 10))

              if (columna == 9):
                  columna = 8

              huecos = 0

              for i in range(3):
                if (carton[i][columna] == 0):
                  huecos = huecos + 1

                if (carton[i][columna] == numero):
                  huecos = 0
                  break

              if (huecos < 2):
                continue

              fila = 0

              for j in range(3):
                huecos = 0
                for i in range(9):
                  if (carton[fila][i] == 0):
                      huecos = huecos + 1

                if (huecos < 5 or carton[fila][columna] != 0):
                  fila = fila + 1
                else:
                  break

              if (fila == 3):
                continue

              carton[fila][columna] = numero
              numerosCarton = numerosCarton + 1
              contador = 0

            for x in range(9):
              huecos = 0
              for y in range(3):
                if (carton[y][x] == 0):
                    huecos = huecos + 1

              if (huecos == 3):
                return carton

            return carton
        mi_carton=carton()
        if (cinco_por_fila(mi_carton) == True and izq_may_der(mi_carton) == True and may_arriba_abajo(mi_carton) == True and may_a_der(mi_carton) == True and no_columna_llena(mi_carton) == True and no_numeros_repetidos(mi_carton) == True and no_tres_ocupadas(mi_carton) == True and no_tres_vacias(mi_carton) == True and filas_con_contenido(mi_carton) == True and columnas_con_contenido(mi_carton) == True and contar_celdas_ocupadas_menores(mi_carton) == True and contar_celdas_ocupadas_mayores(mi_carton) == True and uno_a_noventa(mi_carton) == True):
            a=1
            return mi_carton

imprimirCarton(carton_oficial())
