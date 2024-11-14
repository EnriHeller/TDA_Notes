def bodegon_dinamico(P, W):

    """
        para cada elemento del vector P, tengo un numero y quiero el numero que mas se acerque a W, sin pasarlo. 
    """
    return []

def opt(P,W):

    soluciones = [0]*len(P)

    soluciones[0] = P[0]

    for n in range(1, len(P)):

        if soluciones[n-1] + P[n] <= W:
            soluciones[n] = soluciones[n-1]+P[n]
        else:
            soluciones[n] = soluciones[n-1]

    return soluciones