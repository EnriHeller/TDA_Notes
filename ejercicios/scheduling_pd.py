"""
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla tiene asociado un valor de ganancia. Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad del algoritmo implementado.
"""

#charla[i]= (inicio_i, fin_i, valor_i)

#Si tengo una charla sola, va esa
#Si tengo 2 charlas, va la de mayor valor

#Si tengo 3 charlas, elijo: La hago o no la hago 
    #-> Si la hago, sumo todas las que son compatibles con esta y esta misma 
    #-> Si no, me quedo con la suma que tenia hasta ahora


def scheduling(charlas):
    return []