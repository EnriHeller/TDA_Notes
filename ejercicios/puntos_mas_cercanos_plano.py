def merge(arr1, arr2, p):
    i, j = 0, 0
    res = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i][p] < arr2[j][p]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res.extend(arr1[i:])
    res.extend(arr2[j:])
    
    return res

def merge_sort(puntos, p):
    if len(puntos) <= 1:
        return puntos
    
    medio = len(puntos) // 2
    izq = merge_sort(puntos[:medio], p)
    der = merge_sort(puntos[medio:], p)

    return merge(izq, der, p)

def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def par_minimo(px):
    if len(px) == 3:
        p1, p2, p3 = px

        distancias = [
            (p1, p2, distancia(p1, p2)),
            (p1, p3, distancia(p1, p3)),
            (p2, p3, distancia(p2, p3))
        ]

        return min(distancias, key=lambda x: x[2])[:2]
    
    else:
        return px[0], px[1]

def obtener_sub_arreglos(px, py):
    medio = len(px) // 2
    Qx, Rx = px[:medio], px[medio:]
    x_medio = Qx[-1][0]
    
    Qy = [p for p in py if p[0] <= x_medio]
    Ry = [p for p in py if p[0] > x_medio]
    
    return Qx, Qy, Rx, Ry

def hallar_S(corte, d, py):
    S = [p for p in py if abs(p[0] - corte) < d]
    return S

def puntos_mas_cercanos(puntos):
    px = merge_sort(puntos, 0)
    py = merge_sort(puntos, 1)

    p0, p1 = puntos_mas_cercanos_rec(px, py)

    return p0, p1

def puntos_mas_cercanos_rec(px, py):
    if len(px) <= 3:
        return par_minimo(px)

    Qx, Qy, Rx, Ry = obtener_sub_arreglos(px, py)

    q0, q1 = puntos_mas_cercanos_rec(Qx, Qy)
    r0, r1 = puntos_mas_cercanos_rec(Rx, Ry)

    d = min(distancia(q0, q1), distancia(r0, r1))

    x_corte = Qx[-1][0]

    S = hallar_S(x_corte, d, py)

    p_min = min(
        ((S[i], S[j]) for i in range(len(S)) for j in range(i + 1, min(i + 8, len(S)))),
        key=lambda pair: distancia(pair[0], pair[1]),
        default=(None, None)
    )

    if p_min[0] is not None and distancia(p_min[0], p_min[1]) < d:
        return p_min[0], p_min[1]
    elif distancia(q0, q1) < distancia(r0, r1):
        return q0, q1
    else:
        return r0, r1
