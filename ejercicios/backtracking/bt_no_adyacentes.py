"""
INDEPENDENT SET

Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

"""

def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    vertices = grafo.obtener_vertices()
    res = []
    if rec_no_adyacentes(grafo, vertices, 0, res, n):
        return res
    return None

def es_compatible(grafo, res, nuevo_v):
    for w in res:
        if grafo.estan_unidos(nuevo_v, w):
            return False
    return True

def rec_no_adyacentes(grafo, vertices, v, res, n):
    # Caso base: si logramos construir un conjunto independiente de tamaño n, lo devolvemos.
    if len(res) == n:
        return True

    # Caso de límite: si ya exploramos todos los vértices sin éxito, retornamos False.
    if v == len(vertices):
        return False

    # Intentar incluir el vértice actual si es compatible
    if es_compatible(grafo, res, vertices[v]):
        res.append(vertices[v])

        # Si al incluir el vértice logramos una solución, devolvemos True.
        if rec_no_adyacentes(grafo, vertices, v + 1, res, n):
            return True

        # Backtracking: quitamos el vértice actual y probamos sin él.
        res.pop()

    # Intentamos sin incluir el vértice actual.
    return rec_no_adyacentes(grafo, vertices, v + 1, res, n)
