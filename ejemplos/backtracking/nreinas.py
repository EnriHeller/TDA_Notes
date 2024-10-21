import networkx as nx
import time

DIMENSION = 4

def n_reinas(n):
    casillero = lambda i, j: str(i + 1) + chr(ord('a') + j)
    g = nx.Graph()
    for i in range(n):
        for j in range(n):
            g.add_node(casillero(i, j))

    # Agrego adyacencia por fila
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                g.add_edge(casillero(i, j), casillero(i, k))
    # Agrego por columnas
    for j in range(n):
        for i in range(n):
            for k in range(i+1, n):
                g.add_edge(casillero(i, j), casillero(k, j))

    # agrego por diagonales
    for i in range(n):
        for j in range(n):
            for k in range(i):
                if k < j:
                    g.add_edge(casillero(i, j), casillero(i - k - 1, j - k - 1))
                if k + j + 1 < n:
                    g.add_edge(casillero(i, j), casillero(i - k - 1, j + k + 1))
    return g


def es_compatible(grafo, puestos, ultimo_puesto):
    for w in puestos:
        if ultimo_puesto == w:
            continue
        if grafo.has_edge(ultimo_puesto, w):
            return False
    return True

def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
    if v_actual == len(grafo):
        return False
    if len(puestos) == n:
        return True

    # Mis opciones son poner acá, o no
    puestos.add(vertices[v_actual])
    if es_compatible(grafo, puestos, vertices[v_actual]) and _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n)


def ubicacion(grafo, n):
    puestos = set()
    vertices = list(grafo.nodes)

    _ubicacion_BT(grafo, vertices, 0, puestos, n)

    return puestos


if __name__ == "__main__":
    inicio = time.time()
    print(ubicacion(n_reinas(DIMENSION), DIMENSION))  # https://drive.google.com/file/d/1_j6XaxVGBtJiEmtORGmZimuOvvwJG5ad/view?usp=sharing
    fin = time.time()
    print(int((fin - inicio) * 1000), "mili sec")
