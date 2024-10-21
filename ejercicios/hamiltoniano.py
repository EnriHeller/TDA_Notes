def camino_hamiltoniano(grafo):
    vertices = set(grafo.obtener_vertices())
    v = vertices[0]
    camino = []
    if dfs_hamiltoniano(grafo, v, set(), camino, vertices):
        return camino
    return []

def dfs_hamiltoniano(grafo, v, visitados, camino, vertices):

    visitados.add(v)
    camino.append(v)

    if len(visitados) == len(vertices):
        return True

    for w in grafo.adyacentes(v):
        if w not in visitados: #Poda
            if dfs_hamiltoniano(grafo, w, visitados, camino, vertices):
                return True
    
    visitados.remove(v)
    camino.pop()
    return False