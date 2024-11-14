#elem = (valor, peso)
IDX_VALOR = 0
IDX_PESO = 1


def mochila_pd(elementos, W):
    #Construyo matriz donde considero todos los pesos de 0 a W, para todo el rango de elementos. Es decir, voy a definir el optimo de considerar o no un elemento para las mochilas de todos los pesos posibles de 0 a W
    matriz = [[0 for j in range(W + 1)] for i in range(len(elementos) + 1)]
    for i in range(1, len(elementos) + 1):
        elem = elementos[i-1]
        for j in range(1, W + 1):
            if elem[IDX_PESO] > j:
                matriz[i][j] = matriz[i-1][j] # Si el peso del elemento supera al W actual, lo descarto
            else:
                #Si no, me quedo con el maximo entre no considerar el elemento para el peso actual o el optimo para una mochila de tamaño tal que no considere el peso de este elemento mas el valor actual del elemento. 
                matriz[i][j] = max(matriz[i-1][j], matriz[i-1][j - elem[IDX_PESO]] + elem[IDX_VALOR])
    return matriz[len(elementos)][W]
