def lunatico(ganancias):
    if len(ganancias) == 1:
        return [0]  # Si solo hay una casa, esa es la única opción para robar.
    
    # Resolver excluyendo la casa 0 y excluyendo la casa n-1
    indices_excluyendo_primera = resolver(ganancias[1:])  # Excluimos casa 0
    indices_excluyendo_primera = [i + 1 for i in indices_excluyendo_primera]  # Ajustamos los índices

    indices_excluyendo_ultima = resolver(ganancias[:-1])  # Excluimos casa n-1
    
    # Escoger la solución con mayor ganancia
    if suma(ganancias, indices_excluyendo_primera) > suma(ganancias, indices_excluyendo_ultima):
        return indices_excluyendo_primera
    else:
        return indices_excluyendo_ultima

def resolver(ganancias):
    n = len(ganancias)
    if n == 0:
        return []
    elif n == 1:
        return [0]

    # Tabla de programación dinámica para guardar soluciones
    dp = [0] * n
    dp[0] = ganancias[0]
    
    if n > 1:
        dp[1] = max(ganancias[0], ganancias[1])

    # Crear la tabla de soluciones
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + ganancias[i])

    # Reconstruir los índices de las casas que debemos robar
    indices = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            indices.append(i)
            i -= 2  # Si robamos esta casa, no podemos robar la anterior
        else:
            i -= 1  # No robamos esta casa, pasamos a la anterior
    
    indices.reverse()  # Para devolver en orden de menor a mayor
    return indices

def suma(ganancias, indices):
    return sum(ganancias[i] for i in indices)