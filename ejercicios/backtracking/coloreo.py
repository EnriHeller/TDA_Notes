def colorear(grafo, n):
    v = grafo.vertice_aleatorio()
    colores = {}

    return rec_colorear(grafo,v, colores, n)


def es_compatible(grafo, colores, v):

    for w in grafo.adyacentes(v):
        if w in colores and colores[w] == colores[v]:
            return False
    return True 

def rec_colorear(grafo, v, colores, n):

    for color in range(n):
        colores[v] = color

        if not es_compatible(grafo, colores, v):
            continue
        
        correcto = True
        for w in grafo.adyacentes(v):
            if w in colores:
                continue
            if not rec_colorear(grafo, w, colores, n):
                correcto = False
                break
        
        if correcto: 
            return True
    
    del colores[v]
    return False