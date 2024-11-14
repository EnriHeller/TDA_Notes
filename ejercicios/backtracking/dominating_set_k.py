def dominating_set_k(grafo, k):
    D = []
    vertices = grafo.obtener_vertices()
    cubiertos = set()
    if dominating_rec(vertices, D, 0, grafo, cubiertos, k):
        return D
    else:
        return []

def dominating_rec(vertices, D, i, G, cubiertos, k):
    # Si todos los vértices están cubiertos
    if len(cubiertos) == len(vertices):
        return True

    if len(D) >= k or i == len(vertices):
        return False

    # Intentar agregar el vértice vertices[i] al conjunto dominante
    D.append(vertices[i])
    cubiertos_original = cubiertos.copy()  # Guardar el estado actual

    cubiertos.add(vertices[i])
    for w in G.adyacentes(vertices[i]):
        cubiertos.add(w)

    if dominating_rec(vertices, D, i+1, G, cubiertos, k):
        return True

    # Si no funciona, retroceder (backtracking)
    D.pop()
    cubiertos = cubiertos_original  # Restaurar el estado original

    # Probar sin agregar vertices[i]
    return dominating_rec(vertices, D, i+1, G, cubiertos, k)



