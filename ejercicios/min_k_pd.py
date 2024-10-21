def operaciones(k):
    # Obtenemos la tabla de soluciones usando programación dinámica
    soluciones = sol(k)
    ops = []
    actual = k

    # Seguimos los pasos hacia atrás para encontrar las operaciones
    while actual != 0:
        if actual % 2 == 0 and soluciones[actual // 2] < soluciones[actual - 1]:
            ops.append('por2')
            actual = actual // 2
        else:
            ops.append('mas1')
            actual = actual - 1 

    ops.reverse()  # Invertimos para obtener el orden correcto de operaciones
    return ops

def sol(k):
    # Creamos un arreglo para almacenar las soluciones, donde dp[i] es el mínimo número de operaciones para llegar a i
    dp = [0] * (k + 1)  # dp[0] es 0 porque ya estamos en 0

    for n in range(1, k + 1):
        # Por defecto, la opción es sumar 1 desde n-1
        dp[n] = dp[n - 1] + 1

        # Si n es divisible por 2, consideramos también la opción de duplicar
        if n % 2 == 0:
            dp[n] = min(dp[n], dp[n // 2] + 1)

    return dp

# Ejemplo de uso:
k = 10
print(operaciones(k))  # Salida: ['mas1', 'por2', 'mas1', 'por2', 'por2']
