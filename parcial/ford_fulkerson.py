"""
Se espera recibir un grafo que ya esté adaptado para Ford Fulkerson. Esto es:

    1- Si tiene bucles, los borro
    2- Ciclos de dos vertices, añado un vertice en el medio
    3- Unifico fuentes y sumideros en 1 solo
"""

def obtener_camino():
    pass

def obtener_minima_capacidad():
    pass

def obtener_flujo(grafo, s, t):
    flujo = {}

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0

    red_residual = grafo.copy()

    while True:
        camino = obtener_camino(red_residual, s, t)
        if camino is None:
            break

        minimo = obtener_minima_capacidad(camino, red_residual)

        for i in range(1, len(camino)):
            v, w = camino[i-1], camino[i]

            if grafo.hay_arista(v, w):
                flujo[(v, w)] += minimo
            else:
                flujo[(v, w)] -= minimo

            actualizar_red_residual(red_residual, v, w, minimo)
    
    return flujo

def actualizar_red_residual(grafo, v, w, valor):
    if grafo.hay_arista(v, w):
        peso_original = grafo.obtener_peso_arista(v, w)
        nuevo_peso = peso_original - valor

        if nuevo_peso == 0:
            grafo.remover_arista(v, w)
        else:
            grafo.cambiar_peso_arista(v, w, nuevo_peso)

    if not grafo.hay_arista(w, v):
        grafo.añadir_arista(w, v, valor)
    else:
        peso_v_w = grafo.obtener_peso_arista(w, v)
        grafo.cambiar_peso_arista(w, v, peso_v_w + valor)
