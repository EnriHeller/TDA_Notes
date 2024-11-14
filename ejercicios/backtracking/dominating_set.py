def dominating_set_min(grafo):
    D = []
    vertices = grafo.obtener_vertices()
    cubiertos = set()
    mejor_D = [None]  # Lista para almacenar la mejor solución encontrada (dominating set mínimo)
    dominating_rec(vertices, D, 0, grafo, cubiertos, mejor_D)
    if mejor_D[0] is not None:
        return mejor_D[0]
    else:
        return []

def dominating_rec(vertices, D, i, G, cubiertos, mejor_D):
    # Si todos los vértices están cubiertos
    if len(cubiertos) == len(vertices):
        # Si es la primera solución o si es mejor que la anterior
        if mejor_D[0] is None or len(D) < len(mejor_D[0]):
            mejor_D[0] = D.copy()
        return True

    # Poda: si ya superamos el tamaño de la mejor solución
    if mejor_D[0] is not None and len(D) >= len(mejor_D[0]):
        return False

    if i >= len(vertices):
        return False

    # Incluir vertices[i] en D
    D.append(vertices[i])
    nuevos_cubiertos = cubiertos.copy()
    nuevos_cubiertos.add(vertices[i])
    nuevos_cubiertos.update(G.adyacentes(vertices[i]))

    # Intentar con el vértice actual
    if dominating_rec(vertices, D, i+1, G, nuevos_cubiertos, mejor_D):
        return True

    # Excluir vertices[i] de D
    D.pop()

    # Poda: si no hay suficientes vértices restantes para mejorar la mejor solución
    if mejor_D[0] is None or len(D) + (len(vertices) - i - 1) >= len(mejor_D[0]):
        # Intentar sin el vértice actual
        return dominating_rec(vertices, D, i+1, G, cubiertos, mejor_D)

    return False


