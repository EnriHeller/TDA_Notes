def mochila_con_minimos(elementos, W, K):
    # Llamada inicial a la función recursiva
    return mochila_rec(elementos, K, 0, W, 0, [])

def mochila_rec(elementos, K, i, w_parcial, suma_valores, solucion_actual):

    if i >= len(elementos):
        if len(solucion_actual) >= K:
            return solucion_actual.copy(), suma_valores
        else:
            return [], 0
    
    # Si no es posible formar una solución con al menos K elementos
    faltantes = len(elementos) - i
    if len(solucion_actual) + faltantes < K:
        return [], 0
    
    v = elementos[i]
    mejor_solucion, mejor_valor = solucion_actual.copy(), suma_valores

    # Rama en la que incluimos el elemento actual (si el peso lo permite)
    if v.peso <= w_parcial:
        solucion_actual.append(v)  # Incluir el elemento en la solución
        nuevo_w = w_parcial - v.peso
        nuevo_valor = suma_valores + v.valor

        # Llamada recursiva con el elemento incluido
        nueva_solucion, nueva_suma = mochila_rec(elementos, K, i + 1, nuevo_w, nuevo_valor, solucion_actual)

        # elimino el elemento para probar la rama de exclusión
        solucion_actual.pop()

        # Actualizo si la solución con el elemento incluido es mejor
        if nueva_suma > mejor_valor:
            mejor_solucion, mejor_valor = nueva_solucion, nueva_suma

    # Rama en la que no incluimos el elemento actual
    sin_incluir_solucion, sin_incluir_valor = mochila_rec(elementos, K, i + 1, w_parcial, suma_valores, solucion_actual)

    # Actualizo si la solución sin incluir el elemento es mejor
    if sin_incluir_valor > mejor_valor:
        mejor_solucion, mejor_valor = sin_incluir_solucion, sin_incluir_valor

    return mejor_solucion, mejor_valor
